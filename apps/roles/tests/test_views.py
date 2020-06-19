from django.test import TestCase, Client
from django.urls import reverse
from apps.roles.models import Role

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list_all_role')
        self.search_url = reverse('list_by_key', args=['Credito'])

    
    def test_ListarRoles_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'role/list_all.html')
    
    def test_buscarRoles_GET(self):
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'role/lista_by_key.html')

    def test_crearRoles_POST(self):
        response = self.client.post(reverse('create_role'), {'name_role', 'Contador'})

        self.assertEqual(Role.objects.last().name_role, 'Contador')

    def test_actualizarRoles_POST(self):
        rol = Role.objects.create(name_role='Credito')

        response = self.client.post(
            reverse('update_role', kwargs={'pk': Role.id_role}),
            {'name_role':'Credito2'}
        )

        self.assertEqual(response.status_code, 302)

        Role.refresh_from_db()
        self.assertEqual(Role.name_role, 'Credito2')

    def test_borrarRoles_POST(self):
        response = self.client.get(reverse('delete_role', args=(Role.id_role,)))
        self.assertContains(response, 'Desear Eliminar la Clase')