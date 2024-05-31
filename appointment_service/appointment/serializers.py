from rest_framework import serializers
from .models import Phong, Appointment

class PhongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phong
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    phong = PhongSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentSerializer1(serializers.ModelSerializer):
    phong = serializers.PrimaryKeyRelatedField(queryset=Phong.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'