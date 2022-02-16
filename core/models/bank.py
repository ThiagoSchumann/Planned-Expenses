from django.db import models


# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    logo = models.ImageField(verbose_name='Logomarca')

    class Meta:
        verbose_name = 'Banco'

    def __str__(self):
        return self.name



class BankAccount(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Banco')
    name = models.CharField(max_length=255, verbose_name='Nome')
    opening_balance = models.FloatField(verbose_name='Saldo Inicial')

    class Meta:
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'