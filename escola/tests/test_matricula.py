from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Matricula, Estudante, Curso

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_kaue = Estudante.objects.create(
            nome='Kaue',
            cpf='11122233344',
            data_nascimento='2000-01-01'
        )
        self.estudante_jonas = Estudante.objects.create(
            nome='Jonas',
            cpf='55566677788',
            data_nascimento='2001-02-02'
        )
        self.curso_usinagem = Curso.objects.create(
            codigo='USI01',
            descricao='ASDASDASDASDA',
            nivel='B'
        )
        self.curso_automacao = Curso.objects.create(
            codigo='AUT02',
            descricao='ASDASJDAWYNA',
            nivel='A'
        )
        self.matriculas_01 = Matricula.objects.create(
            estudante = self.estudante_kaue,
            curso = self.curso_usinagem,
            periodo = 'M'
        )
        self.matriculas_02 = Matricula.objects.create(
            estudante = self.estudante_jonas,
            curso = self.curso_automacao,
            periodo = 'N'
        )
    def test_requisicao_get_matriculas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
