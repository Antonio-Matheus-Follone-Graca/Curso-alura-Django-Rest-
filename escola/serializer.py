# importando serializer, é o processo de transformar dados em um formato que pode ser armazenado ou transmitido e, então, reconstruído.
from rest_framework import serializers

#importando models

from escola.models import Aluno,Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    # informando qual classe de model a classe  AlunoSerializer irá utilizar e seus respectivos campos
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    # informando qual classe  de model a classe  AlunoSerializer irá utilizar e seus respectivos campos
    class Meta:
        model = Curso
        # todos os campos
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    # informando qual classe de model a classe  AlunoSerializer irá utilizar e seus respectivos campos
    class Meta:
        model = Matricula
        exclude = []# pega todos os campos o exclude vazio

# listando matriculas por aluno 

class ListandoMatriculasporAlunoSerializer(serializers.ModelSerializer):
    # informando que o campo curso será apenas do tipo leitura e será representado pelo seu campo descrição
    # pois caso contrário será representado pelo seu id
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()
    # definindo qual model o serializer irá utilizar
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    
    # ao usar a função SerializerMethodField DEVE-SE criar um metodo com get_variavel que guarda o SerializerMethodField
    def get_periodo(self, objeto):
        '''
            funcao que pega o nome do periodo e não a sigla
        '''
        return objeto.get_periodo_display() 

