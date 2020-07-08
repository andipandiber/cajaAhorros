from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.roles.models import Role
from .managers import userManager



class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('username', max_length=10, unique=True)
    email = models.EmailField('email', unique=True)
    IDCard = models.CharField('id',max_length=45, unique=True, blank = True)
    name = models.CharField('nombres',max_length=120, blank = True)
    last_name = models.CharField('apellidos',max_length=120, blank = True)
    address = models.CharField('direccion',max_length=500, blank = True)
    phone = models.CharField('telefono' , max_length=45, blank = True)
    dateBirth = models.DateField('fechaNacimiento', auto_now=False, auto_now_add=False)
    codeRegister = models.CharField(max_length=6, blank = True)
    roles = models.ManyToManyField(Role)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'dateBirth']

    objects = userManager()

    def get_shortName(self):
        return self.username

    def get_fullName(self):
        return self.name +' '+ self.last_name


