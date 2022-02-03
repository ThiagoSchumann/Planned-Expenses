from auditlog.registry import auditlog
from django.db import models


# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField()


auditlog.register(Bank)


class BankAccount(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=255)
    opening_balance = models.FloatField()


auditlog.register(BankAccount)