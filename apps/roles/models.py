from django.db import models

class Role(models.Model):
    id_role = models.AutoField('idRole', primary_key = True)
    name_role = models.CharField('nameRole', max_length = 100)

    def __str__(self):
        return str(self.id_role)+' '+self.name_role
