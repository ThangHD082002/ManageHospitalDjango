

# from rest_framework import serializers
# from .models import Fullname, Address, Account, User


# class FullnameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Fullname
#         fields = '__all__'

# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = '__all__'

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     full_name = FullnameSerializer()
#     account = AccountSerializer()
#     address = AddressSerializer()

#     class Meta:
#         model = User
#         fields = '__all__'


# class UserSerializer1(serializers.ModelSerializer):
#     full_name = serializers.PrimaryKeyRelatedField(queryset=Fullname.objects.all())
#     account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
#     address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

#     class Meta:
#         model = User
#         fields = '__all__'






# user/serializers.py

from rest_framework import serializers
from .models import Fullname, Address, Account, User, Identify, Career



class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class IdentifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identify
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    full_name = FullnameSerializer()
    account = AccountSerializer()
    address = AddressSerializer()
    carrer = CareerSerializer(required=False, allow_null=True)
    identify = IdentifySerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = '__all__'

class UserSerializer1(serializers.ModelSerializer):
    full_name = serializers.PrimaryKeyRelatedField(queryset=Fullname.objects.all())
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
    career = serializers.PrimaryKeyRelatedField(queryset=Career.objects.all(), required=False, allow_null=True)
    identify = serializers.PrimaryKeyRelatedField(queryset=Identify.objects.all(), required=False, allow_null=True)

    class Meta:
        model = User
        fields = '__all__'
