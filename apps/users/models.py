from django.db import models


from apps.roles.models import Role

class Persona(models.Model):
    codigo = models.AutoField('ID',primary_key=True)
    cedula = models.CharField('cedula',max_length=45, unique=True)
    nombre = models.CharField('nombres',max_length=120)
    apellido = models.CharField('apellidos',max_length=120)
    direccion = models.CharField('direccion',max_length=500)
    telefono = models.CharField('telefono' , max_length=45)
    date = models.DateField('fechaNacimiento', auto_now=False, auto_now_add=False)
    email = models.EmailField('email', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.codigo)+'-'+self.cedula+'-'+self.nombre+'-'+self.apellido


class Usuario(Persona):
    id_Usuario = models.IntegerField('IdUsuario')
    created_at = models.DateTimeField('fechaInicio', auto_now=False, auto_now_add=True)
    modificated = models.DateTimeField('fechaFin', auto_now=True, auto_now_add=False, null=True, blank= True)
    id_role= models.ManyToManyField(Role)

    class Meta:
        verbose_name = 'user'
        ordering = ['created_at']

    def __str__(self):
       return  str(self.codigoUser)


class Socio(Persona):
    id_Socio = models.IntegerField('idSocio')
    created_at = models.DateTimeField('fechaInicio', auto_now=False, auto_now_add=True)
    modificated = models.DateTimeField('fechaFin', auto_now=True, auto_now_add=False, null=True, blank=True)


    class Meta:
        verbose_name = 'partner'
        ordering = ['created_at']

    def __str__(self):
        return str(self.codigoSocio)

