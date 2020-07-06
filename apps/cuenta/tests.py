from django.test import TestCase, Client
from django.urls import reverse

from apps.cuenta.models import Cuenta


class TestModelCuenta(TestCase):

    def setUp(self):
        self.client = Client()
        self.cuenta = Cuenta.objects.create(
            fecha_apertura = '19/03/2020'
        )

    def test_String_Cuenta(self):
        self.assertEquals(self.fecha_apertura, '19/03/2020')
