from django.db import models
from django.utils import timezone
# Create your models here.



class Examination(models.Model):
    title = models.CharField(max_length=255)
    timeStart = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    doctor = models.IntegerField()

    class Meta:
        verbose_name = "examination"


class PatientExamination(models.Model):
    patient = models.IntegerField()

    class Meta:
        verbose_name = "patient_examination"

class ItemPatientExamination(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    patient_examination = models.ForeignKey(PatientExamination, on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    class Meta:
        verbose_name = "item_patient_examination"