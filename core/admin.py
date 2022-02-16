from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from .models import Expanse, Bank, BankAccount, Transaction


AdminSite.site_header = '💰 Planned Expenses 💰'


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
