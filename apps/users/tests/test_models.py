from django.test import TestCase, Client
from django.urls import reverse
from apps.users.models import Usuario, Socio


class TestModelsUser(TestCase):

    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create(
            cedula = '0150384980',
            nombre = 'Andres',
            apellido = 'Bermeo',
            direccion = 'Sangurima',
            telefono = '2841476',
            date = '30/09/1995',
            email = 'andres@gmail.com'
        )
        self.socio = Socio.objects.create(
            cedula = '0150384981',
            nombre = 'Juan',
            apellido = 'Guillen',
            direccion = 'El Vergel',
            telefono = '2827689',
            date = '10/02/1990',
            email = 'juan@gmail.com'
        )

    
    def test_String_Usuario(self):
        self.assertEqual(self.cedula, '0150384980')
    
    def test_String_Socio(self):
        self.assertEqual(self.cedula, '0150384981')