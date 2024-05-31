from django.db import models

# Create your models here.


class Phong(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Phong"

class Appointment(models.Model):
    title = models.CharField(max_length=255)
    customer = models.IntegerField()
    doctor = models.IntegerField()
    timeStart = models.DateTimeField(null=True, auto_now=True)
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE)
    STATES_CHOICES = [
        ('Cho kham', 'Cho kham'),
        ('Dang kham', 'Dang kham'),
        ('Kham xong', 'Kham xong'),
    ]
    state = models.CharField(max_length=20, choices=STATES_CHOICES, default='Cho Kham')