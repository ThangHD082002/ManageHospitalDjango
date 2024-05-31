from rest_framework import serializers
from .models import Producer, Supply, PatientSupply, ItemPatientSupply

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'

class ItemPatientSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPatientSupply
        fields = '__all__'

class SupplySerializer1(serializers.ModelSerializer):
    producer = serializers.PrimaryKeyRelatedField(queryset=Producer.objects.all())

    class Meta:
        model = Supply
        fields = '__all__'

class PatientSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSupply
        fields = '__all__'

class ItemPatientSupplySerializer1(serializers.ModelSerializer):
    supply = serializers.PrimaryKeyRelatedField(queryset=Supply.objects.all())
    patient_supply = serializers.PrimaryKeyRelatedField(queryset=PatientSupply.objects.all())

    class Meta:
        model = ItemPatientSupply
        fields = '__all__'
