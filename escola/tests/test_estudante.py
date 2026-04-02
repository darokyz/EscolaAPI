from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Estudante

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Marina Silva',
            email = 'marina@marina.com',
            cpf = '44984052007',
            data_nascimento = '2025-04-02',
            celular = '89 9999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Jose Carlos',
            email = 'jose@carlos.com',
            cpf = '60287601021',
            data_nascimento = '2023-04-02',
            celular = '99 8999-9999'
        )
    def test_requisicao_get_para_listar_estudante(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)