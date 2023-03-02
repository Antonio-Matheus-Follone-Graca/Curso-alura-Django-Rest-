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
