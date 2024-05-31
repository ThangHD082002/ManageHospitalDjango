from rest_framework import serializers
from .models import Producer, Medicine, PatientMedicine, ItemPatientMedicine

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    class Meta:
        model = Medicine
        fields = '__all__'

class PatientMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicine
        fields = '__all__'

class ItemPatientMedicineSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer()
    patient_medicine = PatientMedicineSerializer()
    class Meta:
        model = ItemPatientMedicine
        fields = '__all__'





class MedicineSerializer1(serializers.ModelSerializer):
    producer = serializers.PrimaryKeyRelatedField(queryset=Producer.objects.all())

    class Meta:
        model = Medicine
        fields = '__all__'

class ItemPatientMedicineSerializer1(serializers.ModelSerializer):
    medicine = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all())
    patient_medicine = serializers.PrimaryKeyRelatedField(queryset=PatientMedicine.objects.all())

    class Meta:
        model = ItemPatientMedicine
        fields = '__all__'
