from django.db import models

from apps.transaccion.models import Transaccion
from apps.users.models import Socio


class Cuenta(models.Model):
    id_cuenta = models.AutoField('idCuenta', primary_key = True)
    fecha_apertura = models.DateField('fechaApertura', auto_now=False, auto_now_add=False)
    id_transaccion = models.ManyToManyField(Transaccion)
    id_Socio = models.ManyToManyField(Socio)

    class Meta:
        verbose_name = 'accounts'

    def get_Saldo(self):
        return str(self.id_transaccion)


