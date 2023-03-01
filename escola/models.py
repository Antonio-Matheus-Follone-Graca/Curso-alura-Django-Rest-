from django.db import models

# Create your models here.
<<<<<<< HEAD

class Aluno(models.Model):
    nome = models.CharField(max_length= 30)
    rg = models.CharField(max_length= 9)
    cpf = models.CharField(max_length= 11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

# criando model curso

class Curso(models.Model):
    # escolhas de nivel do curso
    NIVEL =(
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A','Avançado')
    )
    codigo_curso = models.CharField(max_length= 10)
    descricao = models.CharField(max_length= 100)
    nivel = models.CharField(max_length=1, choices= NIVEL, blank= False, null= False, default='B')
         

    def __str__(self) :
        return self.descricao
=======
>>>>>>> parent of efc6418 (criando tabelas Curso e Aluno)
