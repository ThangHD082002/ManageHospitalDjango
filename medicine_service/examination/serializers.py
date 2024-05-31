from rest_framework import serializers
from .models import Examination, PatientExamination, ItemPatientExamination

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'

class PatientExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientExamination
        fields = '__all__'


class ItemPatientExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPatientExamination
        fields = '__all__'        

class ItemPatientExaminationSerializer1(serializers.ModelSerializer):
    examination = serializers.PrimaryKeyRelatedField(queryset=Examination.objects.all())
    patient_examination = serializers.PrimaryKeyRelatedField(queryset=PatientExamination.objects.all())

    class Meta:
        model = ItemPatientExamination
        fields = '__all__'
