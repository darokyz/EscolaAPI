from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Curso

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(
            codigo = 'Poo_1',
            descricao = 'qualquer coisa',
            nivel = 'B'
        )
        self.curso_02 = Curso.objects.create(
            codigo = 'Poo_2',
            descricao = 'outras coisas',
            nivel = 'B'
        )
    def test_requisicao_get_para_listar_cursos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)