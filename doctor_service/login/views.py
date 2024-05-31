from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from doctor.models import User
from doctor.serializers import UserSerializer

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not (username and password):
        return Response({'error': 'Vui lòng nhập tên đăng nhập và mật khẩu'}, status=status.HTTP_400_BAD_REQUEST)

    # Sử dụng authenticate để xác thực người dùng
    user = authenticate(request, username=username, password=password)

    if user:
        # Lấy đối tượng User tương ứng với 'user'
        try:
            user_instance = User.objects.get(account=user)
        except User.DoesNotExist:
            return Response({'error': 'User instance not found'}, status=status.HTTP_404_NOT_FOUND)

        # Lấy vai trò của người dùng từ đối tượng User
        role = user_instance.role

        # Tạo token và thêm vai trò vào payload của token
        refresh = RefreshToken.for_user(user)
        refresh['role'] = role

        # Serializer đối tượng User
        user_data = UserSerializer(user_instance).data

        return Response(
            {
                'user': user_data, 
                'access_token': str(refresh.access_token), 
                'refresh_token': str(refresh),
                'message': "Login Success"
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response({'message': 'Login Failed'}, status=status.HTTP_401_UNAUTHORIZED)