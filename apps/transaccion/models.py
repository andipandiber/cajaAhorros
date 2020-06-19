from django.db import models

from apps.solicitud.models import Solicitud

class Transaccion(models.Model):

    TYPE_CHOICES=(
        ('R', 'Retiro'),
        ('D', 'Deposito')
    )
    id_transaccion = models.AutoField('idTransaccion', primary_key = True)
    valor = models.DecimalField('valorTransaccion', max_digits=10, decimal_places=4)
    tipo_transaccion = models.CharField('tipoTransaccion', max_length = 1, choices = TYPE_CHOICES)
    idSolicitud = models.ManyToManyField(Solicitud)

    class Meta:
        verbose_name = 'transacciones'
    
    