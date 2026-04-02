from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudantesSerializer, ListaMatriculaCursosSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.throttling import UserRateThrottle


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post",]



class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    # def get_queryset(self):
    #     queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
    #     return queryset
    # serializer_class = ListaMatriculaCursosSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Matricula.objects.none()  # Swagger agradece 😄

        return Matricula.objects.filter(
            curso_id=pk
        ).order_by("id")
        serializer_class = ListaMatriculaCursosSerializer