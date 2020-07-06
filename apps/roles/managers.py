from django.db import models


class RoleManager(models.Manager):
    

    def list_roles(self):
        return self.all()

    def search_role(self, kword):
        result = self.filter(
            name_role__icontains = kword
            )
        return result

        

