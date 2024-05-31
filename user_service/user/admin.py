from django.contrib import admin
from .models import Fullname, Address, Account, User

# Register your models here.


admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(Account)
admin.site.register(User)
