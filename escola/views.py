from rest_framework import viewsets, generics
# importando models 
from escola.models import Aluno,Curso, Matricula
# importando arquivo de serializer
from escola.serializer import AlunoSerializer,AlunoSerializerV2,CursoSerializer, MatriculaSerializer, ListandoMatriculasporAlunoSerializer, ListaAlunoMatriculadosSerializer

from rest_framework.response import Response
from rest_framework import status

# importando autentição do rest framework
#from rest_framework.authentication import BasicAuthentication

#from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

# DjangoModelPermissions permissões de usuários

# classe do rest framewerork, nome ViewSet é obrigatório 
class AlunosViewSet(viewsets.ModelViewSet):
    '''
        exibindo todos os alunos e alunas
    '''
    # pegando todos os alunos do banco de dados 
    queryset = Aluno.objects.all()
    # função que define qual serializer e versão irei usar
    def get_serializer_class(self):
        if self.request.version == 'v2':
            # utiliza o serializer versão 2
            return AlunoSerializerV2
        
        # senão usa a versão 1
        else:
            return AlunoSerializer
        
class CursosViewSet(viewsets.ModelViewSet):
    '''
        exibindo todos os cursos
    '''
    #   pegando todos os cursos do banco de dados 
    queryset = Curso.objects.all()
    # classe de serializer
    serializer_class = CursoSerializer
    # usando response
    def create(self, request):
        # pegando todos os dados da requisição
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            # salvando o serializer
            serializer.save()
            response = Response(serializer.data, status = status.HTTP_201_CREATED)
            id = str(serializer.data['id'] )
            # criando response location
            response['Location'] = request.build_absolute_uri() + id # endereço da url com o id junto
            return response

   
class MatriculaViewSet(viewsets.ModelViewSet):
    '''
        exibindo todas as matriculas
    '''
    queryset = Matricula.objects.all()
    # classe de serializer
    serializer_class = MatriculaSerializer
    # Até o administrador da api não pode  quebrar uma regra de qual método http será usado
    http_method_names=['get','post','put','path']
  
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
    
    
    
       
        


   

