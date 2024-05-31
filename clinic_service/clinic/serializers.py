from rest_framework import serializers
from .models import TypeClinic, Clinic, Bed

class TypeClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeClinic
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    type_clinic = TypeClinicSerializer(read_only=True)

    class Meta:
        model = Clinic
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer(read_only=True)

    class Meta:
        model = Bed
        fields = '__all__'



class ClinicSerializer1(serializers.ModelSerializer):
    type_clinic = serializers.PrimaryKeyRelatedField(queryset=TypeClinic.objects.all())

    class Meta:
        model = Clinic
        fields = '__all__'

class BedSerializer1(serializers.ModelSerializer):
    clinic = serializers.PrimaryKeyRelatedField(queryset=Clinic.objects.all())

    class Meta:
        model = Bed
        fields = '__all__'