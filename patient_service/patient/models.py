from django.db import models
from django.utils import timezone
# Create your models here.


class InputInformation(models.Model):
    bhyt = models.BooleanField(default=False)
    dungtuyen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    mach = models.CharField(max_length=100)
    nhipTho = models.CharField(max_length=100)
    chieuCao = models.CharField(max_length=100)
    canNang = models.CharField(max_length=100)
    thanNhiet = models.CharField(max_length=100)
    bmi = models.CharField(max_length=100)
    tieuSuBenhLi = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("input_information")



class Patient(models.Model):
    title = models.CharField(max_length=255)
    customer = models.IntegerField()
    doctor = models.IntegerField()
    input = models.ForeignKey(InputInformation, on_delete=models.CASCADE)
    chanDoanLamSang = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    ketQua = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    STATES_CHOICES = [
        ('Ngoai tru', 'Ngoai tru'),
        ('Noi tru', 'Noi tru'),
    ]
    state = models.CharField(max_length=20, choices=STATES_CHOICES, default='Ngoai tru')
    room = models.IntegerField(null=True, blank=True)
    bed = models.IntegerField(null=True, blank=True)
    type_room = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Patient"
