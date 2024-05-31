from django.db import models
from django.utils import timezone
# Create your models here.



class Producer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = "producer"


class Supply(models.Model):
    name = models.CharField(max_length=255)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    sl = models.IntegerField()
    price_day = models.FloatField()

    class Meta:
        verbose_name ="supply"

class PatientSupply(models.Model):
    patient = models.IntegerField()

    class Meta:
        verbose_name = "patient_supply"


class ItemPatientSupply(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    patient_supply = models.ForeignKey(PatientSupply, on_delete=models.CASCADE)
    timeStartThue = models.DateTimeField(auto_now=True)
    sl = models.IntegerField()
    note = models.CharField(max_length=255)

    class Meta:
        verbose_name = "item_patient_supply"
