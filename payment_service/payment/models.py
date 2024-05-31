from django.db import models

# Create your models here.

class Payment(models.Model):
    patient = models.IntegerField()
    tamUng = models.CharField(max_length=255)
    bhytThanhToan = models.CharField(max_length=255)
    phaiDong = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Payment"


class ItemPaymentKham(models.Model):
    item_kham = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    STATES_CHOICES = [
        ('Da thanh toan', 'Da thanh toan'),
        ('Chua thanh toan', 'Chua thanh toan'),
    ]
    state = models.CharField(max_length=20, choices=STATES_CHOICES, default='Chua thanh toan')

    class Meta:
        verbose_name = "Item_Payment_Kham"


class ItemPaymentThuoc:
    item_thuoc = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Item_Payment_Thuoc"




