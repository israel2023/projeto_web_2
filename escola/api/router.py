from rest_framework import routers
from escola.api import viewsets


from escola.api.viewsets import AlunosViewsets, CursosViewsets, MatriculaViewsets, ListaMatriculaAluno, ListaAlunoMatriculados

#meu_modelo_router = routers.DefaultRouter()
#meu_modelo_router.register( 'meu_modelo' , viewsets.MeuModeloViewSet)


router = routers.DefaultRouter()
router.register('alunos', viewsets.AlunosViewsets, basename='Alunos')
router.register('cursos', viewsets.CursosViewsets, basename='Cursos')
router.register('matriculas', viewsets.MatriculaViewsets, basename='Matriculas')
router.register('listagem-matriculas', viewsets.ListaAlunoMatriculados, basename='ListaAlunoMatriculado')
router.register('listagem-curso-periodo', viewsets.ListaMatriculaAluno, basename='ListaMatriculaAluno')