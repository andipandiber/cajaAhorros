from django.db import models

from apps.periodoContable.models import DetalleLibroDiario


class PlanCuenta(models.Model):
    id_plan = models.AutoField('idPlan', primary_key = True)
    nombre_cuenta = models.CharField('nombreCuenta', max_length=80)
    tipo = models.CharField('tipoCuenta', max_length=50)
    categoria = models.CharField('categoriaCuenta', max_length=50)
    nivel = models.CharField('nivelCuenta', max_length=50)
    id_detalleLibro = models.ManyToManyField(DetalleLibroDiario)

    class Meta:
        verbose_name = 'PlandeCuentas'



    def get_total(self):
        pass
