
# login/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from user.models import User, Account
from user.serializers import UserSerializer1, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

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



# @api_view(['GET'])
# def get_patient_list(request):
#     # Kiểm tra xem access_token có trong header không
#     access_token = request.headers.get('Authorization')
#     if not access_token:
#         return Response({'error': 'Access token is missing'}, status=status.HTTP_401_UNAUTHORIZED)
    
#     # Thử kiểm tra access_token
#     try:
#         jwt_authentication = JWTAuthentication()
#         authentication_result = jwt_authentication.authenticate(request)
#         if not authentication_result or len(authentication_result) != 2:
#             raise Exception('Invalid access token')
#         user, _ = authentication_result
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

#     # Kiểm tra xem người dùng có quyền Admin không
#     try:
#         user_instance = User.objects.get(username=user.username)
#     except User.DoesNotExist:
#         return Response({'error': 'User instance not found'}, status=status.HTTP_404_NOT_FOUND)

#     if user_instance.role != 'Admin':
#         return Response({'error': 'Access denied. Only Admin can access this resource'}, status=status.HTTP_403_FORBIDDEN)

#     # Trả về danh sách Patient nếu là Admin
#     patients = User.objects.filter(role='Patient')
#     patient_data = UserSerializer(patients, many=True).data
#     return Response({'patients': patient_data}, status=status.HTTP_200_OK)

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_patient_list(request):
    # Kiểm tra xem người dùng có quyền Admin không
    if request.user.role != 'Admin':
        return Response({'error': 'Access denied. Only Admin can access this resource'}, status=status.HTTP_403_FORBIDDEN)

    # Trả về danh sách Patient nếu là Admin
    patients = User.objects.filter(role='Patient')
    patient_data = UserSerializer(patients, many=True).data
    return Response({'patients': patient_data}, status=status.HTTP_200_OK)
