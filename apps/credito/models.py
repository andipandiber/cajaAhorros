from django.db import models

from apps.solicitud.models import Solicitud
from apps.tablasAmortizacion.models import TablasAmortizacion


class Credito(models.Model):
    id_credito = models.AutoField('idCredito', primary_key = True)
    id_Solicitud = models.ManyToManyField(Solicitud)
    id_tablas = models.ManyToManyField(TablasAmortizacion)
    
    class Meta:
        verbose_name = 'Creditos'
