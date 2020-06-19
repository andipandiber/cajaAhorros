from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.roles.views import *


class TestUrls(SimpleTestCase):

    def test_listarRoles(self):
        url = reverse('list_all_role')
        self.assertEquals(resolve(url).func, list_all_role)

    def test_busquedaRoles(self):
        url = reverse('list_by_key')
        self.assertEquals(resolve(url).func, list_key_role)

    def test_crearRoles(self):
        url = reverse('create_role')
        self.assertEquals(resolve(url).func.view_class, create_role)

    def test_actualizarRoles(self):
        url = reverse('update_role')
        self.assertEquals(resolve(url).func.view_class, update_role)

    def test_borrarRoles(self):
        url = reverse('delete_role')
        self.assertEquals(resolve(url).func.view_class, delete_role)



