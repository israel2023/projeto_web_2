from django.contrib import admin
from escola import models
from escola.models import Aluno, Curso, Matricula  #importando aluno e cursos
admin.site.register(models.Post)#Não é relevante, é sobre outra coisa, essa linha

#como eu quero que apareça no django admin
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'rg', 'cpf', 'dataNascimento')
    list_display_links= ('id', 'nome') # Sempre que eu quiser alterar algum valor
    search_fields = ('nome',) #buscar alunos por nome
    list_per_page = 20

#registrando as configurações do meu admin
admin.site.register(Aluno, AlunoAdmin) # modelo(Aluno) e configuração(Alunos)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigoCurso', 'descricao')
    list_display_links = ('id', 'codigoCurso',)
    search_fields = ('codigoCurso',)
    
admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)
    
    
admin.site.register(Matricula, MatriculaAdmin)