from django.contrib import admin
from django.urls import path, include
# importando views
from django.conf import settings
from django.conf.urls.static import static
from escola. views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
# importando rotas do rest framework
from rest_framework import routers

# configurando rotas do rest framework
router = routers.DefaultRouter()
# registrando rotas,sintaxe: prefixo(url), classe viewset e basename (nome / apelido da rota), basename é  (opcional)
router.register('aluno', AlunosViewSet, basename='Alunos')

# cadastrando rota de cursos
router.register('cursos', CursosViewSet, basename='Cursos')


# cadastrando rota de matricula
router.register('matriculas', MatriculaViewSet, basename='Matriculas')


urlpatterns = [
    # usando honey spot
    # tela fake para invasores
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # admin verdadeiro
    path('controle-geral/', admin.site.urls),
    # colocando as rotas do rest framework nas rotas do djnago
    # nesse caso na index do projeto mostrará todas as rotas cadastradas do rest framework 
    path('',include(router.urls)),
    # rota que usa  generics. O as_view() é para informar que é uma view(não sei pq mas só roda assim) 
    path('alunos/<int:pk>/matriculas/',ListaMatriculasAluno.as_view()),
    # outra rota que o serializer usa generics
    path('cursos/<int:pk>/matriculas/',ListaAlunosMatriculados.as_view())

]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


