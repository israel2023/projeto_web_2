from rest_framework import viewsets, permissions, generics
#from escola import models
#from escola.api import serializers
from escola.models import Post, Aluno, Curso, Matricula
from escola.api.permissions import IsInSpecificGroup
from escola.api.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions




"""class MeuModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.MeuModeloSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup]"""

class AlunosViewsets(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    #Fazendo autenticação
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class CursosViewsets(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    #Fazendo autenticação
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class MatriculaViewsets(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    #Fazendo autenticação
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]


"""COLOCAR LA NO VIEWS.PY"""
"""Listar todas as matriculas de alunos"""
class ListaMatriculaAluno(viewsets.ModelViewSet):
    """Listando as matriculas de aluno(a)"""
    def get_queryset(self):
        #queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']).order_by('id') # filtrando busca por lista de matriculas
        queryset = Matricula.objects.all()
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    #Fazendo autenticação
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

"""Listar todos os alunos matriculados em um curso"""
class ListaAlunoMatriculados(viewsets.ModelViewSet):
    """Listando alunos(as) matriculados em um curso"""
    def get_queryset(self):
        #queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        queryset = Matricula.objects.all()
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    #Fazendo autenticação
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]