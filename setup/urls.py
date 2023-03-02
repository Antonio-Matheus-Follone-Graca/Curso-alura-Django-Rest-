from django.contrib import admin
from django.urls import path, include
# importando views
from escola. views import AlunosViewSet, CursosViewSet
# importando rotas do rest framework
from rest_framework import routers

# configurando rotas do rest framework
router = routers.DefaultRouter()
# registrando rotas,sintaxe: prefixo(url), classe viewset e basename (nome / apelido da rota), basename é  (opcional)
router.register('aluno', AlunosViewSet, basename='Alunos')

# cadastrando rota de cursos
router.register('cursos', CursosViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    # colocando as rotas do rest framework nas rotas do djnago
    path('',include(router.urls)) # nesse caso na index do projeto mostrará todas as rotas cadastradas do rest framework 
]


