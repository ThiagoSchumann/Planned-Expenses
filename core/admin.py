from django.contrib import admin
from .models import Expanse, Bank, BankAccount

# Register your models here.
admin.site.register(Expanse)
admin.site.register(Bank)
admin.site.register(BankAccount)
