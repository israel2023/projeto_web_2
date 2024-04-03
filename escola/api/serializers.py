from rest_framework import serializers
from escola import models
from escola.models import Post
from escola.models import Aluno, Curso, Matricula

# Serializer funciona como um filtro na minha API, para mostrar só os dados que eu colocar aqui

class MeuModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'

#projeto escola
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'dataNascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')#para exibir como descrição
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, object):
        return object.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    alunoNome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['alunoNome']