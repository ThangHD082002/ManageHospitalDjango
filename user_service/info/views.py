from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import User, Fullname, Address, Account
from django.shortcuts import get_object_or_404
from user.models import User, Fullname, Address, Account
from user.serializers import UserSerializer,UserSerializer1, FullnameSerializer, AddressSerializer, AccountSerializer
from django.shortcuts import get_object_or_404
import re

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        # Lấy đối tượng User
        user = get_object_or_404(User, id=user_id)
        
        # Lưu lại thông tin liên kết trước khi xóa User
        full_name = user.full_name
        address = user.address
        account = user.account

        # Xóa đối tượng User
        user.delete()

        # Xóa các đối tượng liên kết nếu cần thiết
        if full_name:
            full_name.delete()
        if address:
            address.delete()
        if account:
            account.delete()

        return Response({'message': 'User and related data deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    full_name_data = request.data.get('full_name', {})
    address_data = request.data.get('address', {})
    account_data = request.data.get('account', {})
    role = request.data.get('role', user.role)

    full_name_serializer = FullnameSerializer(user.full_name, data=full_name_data, partial=True)
    address_serializer = AddressSerializer(user.address, data=address_data, partial=True)
    account_serializer = AccountSerializer(user.account, data=account_data, partial=True)

    if full_name_serializer.is_valid() and address_serializer.is_valid() and account_serializer.is_valid():
        full_name_serializer.save()
        address_serializer.save()
        account = account_serializer.save()
        
        if 'password' in account_data:
            password = account_data.get('password', '')
            password_errors = []
            if len(password) < 8:
                password_errors.append('Password must be at least 8 characters long.')
            if not re.search(r'\d', password):
                password_errors.append('Password must contain at least one digit.')
            if not re.search(r'[A-Z]', password):
                password_errors.append('Password must contain at least one uppercase letter.')
            if not re.search(r'[a-z]', password):
                password_errors.append('Password must contain at least one lowercase letter.')
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                password_errors.append('Password must contain at least one special character.')

            if password_errors:
                return Response({'password_errors': password_errors}, status=status.HTTP_400_BAD_REQUEST)

            account.set_password(password)
            account.save()

        user.role = role
        user.save()

        user_data = UserSerializer1(user).data
        return Response(
            {
                'user': user_data,
                'message': "Update Success"
            },
            status=status.HTTP_200_OK
        )
    else:
        errors = {
            'full_name_errors': full_name_serializer.errors,
            'address_errors': address_serializer.errors,
            'account_errors': account_serializer.errors,
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_data = UserSerializer(user).data
    return Response(user_data, status=status.HTTP_200_OK)