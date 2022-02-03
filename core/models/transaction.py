from auditlog.registry import auditlog
from django.db import models
from core.models import Expanse, BankAccount


# Create your models here.


class TransactionStatus(models.IntegerChoices):
    PENDING = 1, 'Pendente'
    SETTLED = 2, 'Liquidada'


class Transaction(models.Model):
    expanse_id = models.ForeignKey(Expanse, on_delete=models.SET_NULL)
    bank_account_id = models.ForeignKey(BankAccount, on_delete=models.SET_NULL)
    due_date = models.DateField()
    settlement_date = models.DateField()
    status = models.IntegerField(default=TransactionStatus.PENDING, choices=TransactionStatus)
    value = models.FloatField()


auditlog.register(Transaction)
