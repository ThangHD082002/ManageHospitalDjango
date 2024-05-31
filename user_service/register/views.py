# from django.shortcuts import render


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from user.models import User, Fullname, Address, Account
# from user.serializers import UserSerializer1, FullnameSerializer, AddressSerializer, AccountSerializer
# # register/views.py

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from user.models import User, Fullname, Address, Account
# from user.serializers import UserSerializer1, FullnameSerializer, AddressSerializer, AccountSerializer
# from django.db import IntegrityError
# import re

# @api_view(['POST'])
# def register(request):
#     full_name_data = request.data.get('full_name')
#     address_data = request.data.get('address')
#     account_data = request.data.get('account')
#     role = request.data.get('role', 'Customer')

#     if not (full_name_data and address_data and account_data):
#         return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

#     password = account_data.get('password', '')
#     if not password:
#         return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
    
#     # Kiểm tra mật khẩu
#     password_errors = []
#     if len(password) < 8:
#         password_errors.append('Password must be at least 8 characters long.')
#     if not re.search(r'\d', password):
#         password_errors.append('Password must contain at least one digit.')
#     if not re.search(r'[A-Z]', password):
#         password_errors.append('Password must contain at least one uppercase letter.')
#     if not re.search(r'[a-z]', password):
#         password_errors.append('Password must contain at least one lowercase letter.')
#     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
#         password_errors.append('Password must contain at least one special character.')

#     if password_errors:
#         return Response({'password_errors': password_errors}, status=status.HTTP_400_BAD_REQUEST)

#     full_name_serializer = FullnameSerializer(data=full_name_data)
#     address_serializer = AddressSerializer(data=address_data)

#     if full_name_serializer.is_valid() and address_serializer.is_valid():
#         full_name = full_name_serializer.save()
#         address = address_serializer.save()

#         # Kiểm tra xem username đã tồn tại chưa
#         if Account.objects.filter(username=account_data['username']).exists():
#             return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Create account and hash the password
#             account = Account(username=account_data['username'], email=account_data['email'])
#             account.set_password(password)
#             account.save()

#             user = User.objects.create(full_name=full_name, address=address, account=account, role=role)
#             user_data = UserSerializer1(user).data

#             return Response(
#                 {
#                     'user': user_data,
#                     'message': "Registration Success"
#                 },
#                 status=status.HTTP_201_CREATED
#             )
#         except IntegrityError:
#             return Response({'message': 'Database error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         errors = {
#             'full_name_errors': full_name_serializer.errors,
#             'address_errors': address_serializer.errors,
#         }
#         return Response(errors, status=status.HTTP_400_BAD_REQUEST)







# register/views.py

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user.models import User, Fullname, Address, Account, Specialty, Identify
from user.serializers import UserSerializer1, FullnameSerializer, AddressSerializer, AccountSerializer, SpecialtySerializer, IdentifySerializer
from django.db import IntegrityError
import re

@api_view(['POST'])
def register(request):
    full_name_data = request.data.get('full_name')
    address_data = request.data.get('address')
    account_data = request.data.get('account')
    role = request.data.get('role', 'Patient')
    specialty_data = request.data.get('specialty')
    identify_data = request.data.get('identify')

    if not (full_name_data and address_data and account_data):
        return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

    password = account_data.get('password', '')
    if not password:
        return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Kiểm tra mật khẩu
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

    full_name_serializer = FullnameSerializer(data=full_name_data)
    address_serializer = AddressSerializer(data=address_data)
    specialty_serializer = SpecialtySerializer(data=specialty_data) if specialty_data else None
    identify_serializer = IdentifySerializer(data=identify_data) if identify_data else None

    if full_name_serializer.is_valid() and address_serializer.is_valid() and (specialty_serializer is None or specialty_serializer.is_valid()) and (identify_serializer is None or identify_serializer.is_valid()):
        full_name = full_name_serializer.save()
        address = address_serializer.save()
        specialty = specialty_serializer.save() if specialty_serializer else None
        identify = identify_serializer.save() if identify_serializer else None

        # Kiểm tra xem username đã tồn tại chưa
        if Account.objects.filter(username=account_data['username']).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create account and hash the password
            account = Account(username=account_data['username'], email=account_data['email'])
            account.set_password(password)
            account.save()

            user = User.objects.create(full_name=full_name, address=address, account=account, role=role, specialty=specialty, identify=identify)
            user_data = UserSerializer1(user).data

            return Response(
                {
                    'user': user_data,
                    'message': "Registration Success"
                },
                status=status.HTTP_201_CREATED
            )
        except IntegrityError:
            return Response({'message': 'Database error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        errors = {
            'full_name_errors': full_name_serializer.errors,
            'address_errors': address_serializer.errors,
        }
        if specialty_serializer:
            errors['specialty_errors'] = specialty_serializer.errors
        if identify_serializer:
            errors['identify_errors'] = identify_serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
