from rest_framework import viewsets
# importando models 
from escola.models import Aluno,Curso
# importando arquivo de serializer
from escola.serializer import AlunoSerializer,CursoSerializer

# classe do rest framewerork, nome ViewSet é obrigatório 
class AlunosViewSet(viewsets.ModelViewSet):
    '''
        exibindo todos os alunos e alunas
    '''
    # pegando todos os alunos do banco de dados 
    queryset = Aluno.objects.all()
    # classe de serializer
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    '''
        exibindo todos os cursos
    '''
    #   pegando todos os cursos do banco de dados 
    queryset = Curso.objects.all()
    # classe de serializer
    serializer_class = CursoSerializer
   

