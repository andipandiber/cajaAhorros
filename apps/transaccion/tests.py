from django.test import TestCase, Client
from django.urls import reverse

from apps.transaccion.models import Transaccion


class Test_ModelsTransaccion(TestCase):

    def setUp(self):
        self.client = Client()
        self.transaccion = Transaccion.objects.create(
            
        )

