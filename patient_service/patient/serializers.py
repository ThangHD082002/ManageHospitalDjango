from rest_framework import serializers
from .models import InputInformation,  Patient

class InputInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputInformation
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    input = InputInformationSerializer()
    class Meta:
        model = Patient
        fields = '__all__'

class PatientSerializer1(serializers.ModelSerializer):
    input = serializers.PrimaryKeyRelatedField(queryset=InputInformation.objects.all())
    class Meta:
        model = Patient
        fields = '__all__'
