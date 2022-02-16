from django.db import models
from core.models import Expanse, BankAccount


# Create your models here.


class TransactionStatus(models.IntegerChoices):
    PENDING = 1, 'Pendente'
    SETTLED = 2, 'Liquidada'


class Transaction(models.Model):
    expanse_id = models.ForeignKey(Expanse,
                                   on_delete=models.PROTECT,
                                   verbose_name='Despesa')
    bank_account_id = models.ForeignKey(BankAccount, on_delete=models.PROTECT, verbose_name='Conta Bancária')
    due_date = models.DateField(verbose_name='Data de Vencimento')
    settlement_date = models.DateField(verbose_name='Data de Liquidação')
    status = models.IntegerField(default=TransactionStatus.PENDING, choices=TransactionStatus.choices, verbose_name='Situação')
    value = models.FloatField(verbose_name='Valor')

    class Meta:
        verbose_name = 'Transação'

