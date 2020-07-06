from django.db import models

from django.contrib.auth.models import BaseUserManager


class userManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, dateBirth, password , is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            dateBirth = dateBirth,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_user(self, username, email, dateBirth, password = None, **extra_fields):
        return self._create_user(username, email, dateBirth, password, False, False, False, **extra_fields)


    def create_superuser(self, username, email, dateBirth, password = None, **extra_fields):
        return self._create_user(username, email, dateBirth, password, True, True, True, **extra_fields)

    def codeValidator(self, id_user, codeRegistration):
        if self.filter(id = id_user, codeRegister = codeRegistration).exists() :
            return True
        else:
            return False

