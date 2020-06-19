from django.db import models

class TablasAmortizacion(models.Model):
    id_tablas = models.AutoField('idTablasAmortizacion', primary_key = True)
    monto = models.DecimalField('montoTablas', max_digits=10, decimal_places=4)
    tipo_credito = models.CharField('tipoCredito', max_length=50)
    meses_plazo = models.CharField('mesesPlazo', max_length=50)
    tipo_transaccion = models.CharField('tipoTransaccion', max_length=50)

    class Meta:
        verbose_name = 'Tablas'


