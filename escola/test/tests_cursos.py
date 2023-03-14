# bibliotecas para testes
from rest_framework.test import APITestCase
#importando model que quero testar
from escola.models import Curso
# reverse do urls
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):
    # método que inicia os testes.Nome da função esse mesmo
    def setUp(self):
        # mostra todas as listas da url de BaseName Cursos
        #a função reverse permite recuperar detalhes do URL do arquivo url's.py por meio do valor do nome fornecido lá. Este é o principal uso da função reversa no Django. A variável de redirecionamento é a variável aqui que terá o valor invertido.
        self.list_url = reverse('Cursos-list')
        # criando curso
        self.curso_1= Curso.objects.create(
            codigo_curso ='CTT1',
            descricao = 'Curso teste 1',
            nivel = 'B'
        )
        # criando curso
        self.curso_2= Curso.objects.create(
            codigo_curso ='CTT2',
            descricao = 'Curso teste 2',
            nivel = 'A'
        )
    
    # metodo test falha, o test_ é obrigatório 
    """  def test_falhador(self):
        self.fail('Teste falhou de propsito´não se preocupe  ') """
    
    # usando verbo get do  http
    def test_requisicao_get_para_listar_cursos(self):
        '''
            teste para verificar  a requisição GET para listar os cursos
        '''
        # fazendo requisição do tipo get
        response = self.client.get(self.list_url)
        # verificando resultado da resposta
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        '''
            teste para verificar  a requisição POST para criar um curso
        '''
        data = {
            'codigo_curso': 'CTT3',
            'descricao' : 'Curso teste 3 ',
            'nivel': 'A'
        }
        # resposta da requisição
        response = self.client.post(self.list_url,data= data)
        # verificando se o test de post está certo
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_para_deletar_curso(self):
        '''
            Teste para verificar a requisição DELETE não permitida para deletar um curso
        '''
        # requisição 
        response = self.client.delete('/cursos/1/')
        # verificacao se  o usuário tentou usar a requisição delete
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_curso(self):
        '''
            Teste para verificar requisição PUT para atualizar um curso
        '''
        dados_atualizados = {
            'codigo_curso': 'CTT1',
            'descricao' : ' Curso teste 1 atualizado',
            'nivel': 'I'
        }
        # requisição para atualizar um curso, rota, dados
        response =  self.client.put('/cursos/1/',data= dados_atualizados)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


        