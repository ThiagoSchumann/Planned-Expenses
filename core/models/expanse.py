from auditlog.registry import auditlog
from django.db import models


# Create your models here.

class Periodicity(models.IntegerChoices):
    MONTHLY = 1, 'Mensal'
    BIMONTHLY = 2, 'Bimestral'
    TRIMONTHLY = 3, 'Trimestral'
    BIANNUAL = 4, 'Semestral'
    ANNUAL = 5, 'Anual'


class Expanse(models.Model):
    next_occurrence = models.DateField()
    periodicity_occurrence = models.IntegerField(default=Periodicity.ANNUAL, choices=Periodicity.choices)
    value = models.FloatField()


auditlog.register(Expanse)
