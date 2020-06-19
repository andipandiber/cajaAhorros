from django.db import models

from apps.users.models import *


class Solicitud(models.Model):
    idSolicitud = models.AutoField('idSolicitud', primary_key = True)
    fecha = models.DateField('fechaSolicitud', auto_now=False, auto_now_add=False)
    idUsuario = models.ManyToManyField(Usuario)
    idSocio = models.ManyToManyField(Socio)

    class Meta:
        verbose_name = 'requests'
