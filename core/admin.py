from django.contrib import admin
from .models import Expanse, Bank, BankAccount, Transaction


# Register your models here.

@admin.register(Expanse)
class ExpanseAdmin(admin.ModelAdmin):
    list_display = ("next_occurrence", "periodicity_occurrence", "value")


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "opening_balance")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("due_date", "settlement_date", "status", "value")
