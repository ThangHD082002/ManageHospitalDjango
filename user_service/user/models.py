# from django.contrib.auth.models import AbstractUser
# from django.db import models


# # user/models.py

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class Fullname(models.Model):
#     ho = models.CharField(max_length=25)
#     ten = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = 'Fullname'




# class Address(models.Model):
#     so_nha = models.CharField(max_length=100)
#     street = models.CharField(max_length=100)
#     ward = models.CharField(max_length=100)
#     district = models.CharField(max_length=100)
#     conscious_city = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = "Address"

# class Account(AbstractUser):
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='account_groups',
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='account_user_permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

#     class Meta:
#         verbose_name = "Account"

# class User(models.Model):
#     ROLES_CHOICES = [
#         ('Doctor', 'Doctor'),
#         ('Patient', 'Patient'),
#         ('Admin', 'Admin'),
#     ]
#     role = models.CharField(max_length=20, choices=ROLES_CHOICES, default='Customer')
#     full_name = models.ForeignKey(Fullname, on_delete=models.CASCADE)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)





# user/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Fullname(models.Model):
    ho = models.CharField(max_length=25)
    ten = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Fullname'

    def __str__(self):
        return f"{self.ho} {self.ten}"

class Address(models.Model):
    so_nha = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    conscious_city = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Address"

    def __str__(self):
        return f"{self.so_nha}, {self.street}, {self.ward}, {self.district}, {self.conscious_city}"

class Account(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='account_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='account_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = "Account"

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"

    def __str__(self):
        return self.name

class Identify(models.Model):
    so_the = models.CharField(max_length=100)
    ngay_cap = models.DateField()

    class Meta:
        verbose_name = "Identify"

    def __str__(self):
        return f"{self.so_the} - {self.ngay_cap}"

class User(models.Model):
    ROLES_CHOICES = [
        ('Admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default='Patient')
    full_name = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True, blank=True)
    identify = models.ForeignKey(Identify, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "User"

    def save(self, *args, **kwargs):
        if self.role != 'Doctor':
            self.specialty = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.get_role_display()}"