from django.db import models

from apps.transaccion.models import Transaccion

class LibroDiario(models.Model):
    id_libro = models.AutoField('idLibro', primary_key = True)
    num_asiento = models.IntegerField()
    fecha = models.DateField('fecha', auto_now=False, auto_now_add=False)
    descripcion = models.CharField('descripcion', max_length=100)
    id_transaccion = models.ManyToManyField(Transaccion)

    class Meta:
        verbose_name = 'LibroDiario'


    def get_total_deber(self):
        pass

    def get_total_haber(self):
        pass


class DetalleLibroDiario(models.Model):
    id_detalle = models.AutoField('idDetalle', primary_key = True)
    debe = models.DecimalField('debe', max_digits=10, decimal_places=4)
    haber = models.DecimalField('haber', max_digits=10, decimal_places=4)
    id_libro = models.ManyToManyField(LibroDiario)



class PeriodoContable(models.Model):
    id_periodo = models.AutoField('idPeriodo', primary_key = True)
    fechaInicio = models.DateField('fechaInicioPeriodo', auto_now=False, auto_now_add=False)
    fechaFin = models.DateField('fechaFinPeriodo', auto_now=False, auto_now_add=False)
    id_detalle = models.ForeignKey(DetalleLibroDiario, on_delete=models.CASCADE)