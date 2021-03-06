from django.db import models


# Create your models here.

class Periodicity(models.IntegerChoices):
    MONTHLY = 1, 'Mensal'
    BIMONTHLY = 2, 'Bimestral'
    TRIMONTHLY = 3, 'Trimestral'
    BIANNUAL = 4, 'Semestral'
    ANNUAL = 5, 'Anual'


class Expanse(models.Model):
    description = models.CharField(max_length=255,
                                   verbose_name='Descrição')
    next_occurrence = models.DateField(verbose_name='Próxima Ocorrência')
    periodicity_occurrence = models.IntegerField(default=Periodicity.ANNUAL,
                                                 choices=Periodicity.choices,
                                                 verbose_name='Periodicidade')
    value = models.FloatField(verbose_name='Valor')

    class Meta:
        verbose_name = 'Despesa'

    def __str__(self):
        return self.name