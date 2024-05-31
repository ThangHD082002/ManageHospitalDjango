from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import  User



from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail

@api_view(['POST'])
def send_reset_password_email(request):
    email = request.data.get('email')

    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(account__email=email)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Tạo token để đặt lại mật khẩu
    token = default_token_generator.make_token(user.account)

    # Gửi email với liên kết để đặt lại mật khẩu
    subject = 'Reset Your Password'
    message = f'Please click the link below to reset your password:\n\n{request.build_absolute_uri(reverse("reset-password"))}?uidb64={urlsafe_base64_encode(force_bytes(user.account.pk)).decode()}&token={token}'
    send_mail(subject, message, 'from@example.com', [email])

    return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_password(request):
    uidb64 = request.data.get('uidb64')
    token = request.data.get('token')
    new_password = request.data.get('new_password')

    if not (uidb64 and token and new_password):
        return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)
