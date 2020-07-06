from django.test import TestCase, Client
from django.urls import reverse
from apps.solicitud.models import Solicitud

class TestViewSolicitud(TestCase):

    def setUp(self):
        self.client = Client()
        self.solicitud = Solicitud.objects.create(
            fecha = '28/06/2020'
        )


    def test_string_Solicitud(self):
        self.assertEquals(self.fecha, '28/06/2020')
