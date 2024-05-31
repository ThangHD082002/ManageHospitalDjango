from django.db import models

# Create your models here.



class Producer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Producer"

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    sl = models.IntegerField()
    note = models.CharField(max_length=255)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    gia = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Medicine"


class PatientMedicine(models.Model):
    patient = models.IntegerField()

    class Meta:
        verbose_name = "patient_medicine"


class ItemPatientMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    sl = models.IntegerField()
    note = models.CharField(max_length=255)
    patient_medicine = models.ForeignKey(PatientMedicine, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "item_patient_medicine"


    
