from rest_framework import viewsets, generics
# importando models 
from escola.models import Aluno,Curso, Matricula
# importando arquivo de serializer
from escola.serializer import AlunoSerializer,CursoSerializer, MatriculaSerializer, ListandoMatriculasporAlunoSerializer, ListaAlunoMatriculadosSerializer

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


class MatriculaViewSet(viewsets.ModelViewSet):
    '''
        exibindo todas as matriculas
    '''
    queryset = Matricula.objects.all()
    # classe de serializer
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    # generics possui funções mais faceis para mapear o banco de dados 
    '''
        listando matriculas de um aluno(a)
    '''
    # em generics deve-se usar um método query set na forma abaixo 
    def get_queryset(self):
        # pegando todas as matriculas por aluno
        # pk = id e o este nome, deve ser igual ao da urls.py de setup
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
        #  classe de serializer
    serializer_class = ListandoMatriculasporAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    '''
        Listando alunos e alunas matriculados em um curso
    ''' 
    # em generics deve-se usar um método query set na forma abaixo 
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset

    # classe de serializer
    serializer_class = ListaAlunoMatriculadosSerializer
    
       
        


   

