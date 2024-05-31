from django.db import models

class TypeClinic(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
       verbose_name = "type_clinic"

    

class Clinic(models.Model):
    ten = models.CharField(max_length=255)
    type_clinic = models.ForeignKey(TypeClinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

    class Meta:
       verbose_name = "clinic"

class Bed(models.Model):
    name = models.CharField(max_length=255)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "bed"
