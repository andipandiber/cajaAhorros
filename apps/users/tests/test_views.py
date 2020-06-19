from django.test import TestCase, Client
from django.urls import reverse

from apps.users.models import Usuario, Socio

class TestViewsUser(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('user_all')
        self.search_url = reverse('userRoles', args=['0150384980'])


    def test_crearUsuarios_POST(self):
        response = self.client.post(reverse('createUser'), {
            'cedula' : "0150384980",
            'nombre' : "Andres",
            'apellido' : "Bermeo",
            'direccion' : "Sangurima",
            'telefono' : "2841476",
            'date' : "30/09/1995",
            'email' : "andres@gmail.com"
        })
        self.assertEqual(Usuario.objects.last().cedula, '0150384980')

    
    def test_actualizarUsuarios_POST(self):
        usuario = Usuario.objects.create(
            cedula = "0150384980",
            nombre = "Andres",
            apellido = "Bermeo",
            direccion = "Sangurima",
            telefono = "2841476",
            date = "30/09/1995",
            email = "andres@gmail.com"
        )

        response = self.client.post(
            reverse('updateUser', kwargs={'pk': Usuario.cedula}),
            {'cedula' : "0150384980",
            'nombre' : "Juan",
            'apellido' : "Bermeo",
            'direccion' : "Sangurima",
            'telefono' : "2841476",
            'date' : "30/09/1995",
            'email' : "andres@gmail.com"}
        )

        self.assertEqual(response.status_code, 302)

        Usuario.refresh_from_db()
        self.assertEqual(Usuario.nombre, 'Juan')
    
    def test_borrarUsuario_POST(self):
        response = self.client.get(
            reverse('deleteUser', args=(Usuario.cedula))
        )
        self.assertContains(response, 'Desea Eliminar el Usuario')

    def test_listarUsuarios_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'persona/list_all.html')

    def test_buscarRoles_GET(self):
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'persona/list_by_key.html')