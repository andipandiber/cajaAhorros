from django.test import TestCase

from apps.roles.models import Role


class TestModels(TestCase):

    def setUp(self):
        self.role1 = Role.objects.create(
            name_role = 'Contador'
        )

    def test_stringValidacion(self):
        self.assertEqual(str(self.role1), 'Contador')