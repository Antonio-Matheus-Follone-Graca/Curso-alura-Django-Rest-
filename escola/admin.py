from django.contrib import admin

# Register your models here.

from escola.models import Aluno,Curso, Matricula
# Register your models here.

# mudanças envolvendo Alunos
class Alunos(admin.ModelAdmin):
    # campos que quero exibir no admin da tabela aluno
    list_display = ('id','nome','rg','cpf','data_nascimento')
    # links para alterar alunos pelos campos id e nome
    list_display_links = ('id','nome')
    # busca por campo
    search_fields = ('nome',) # , é obrigatório no final 
    list_per_page = 20



# registrando mudanças no admin
admin.site.register(Aluno,Alunos)

# mudanças envolvendo Cursos

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao','nivel')
    list_display_links =('id','codigo_curso')
    search_fields = ('codigo_curso',) # , é obrigatório no final 

# registrando mudanças no admin
admin.site.register(Curso, Cursos)

# registrando mudanças no admin envolvendo Matricula
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'curso', 'periodo')
    list_display_links = ('id',)

# registrando mudanças no admin
admin.site.register(Matricula, Matriculas)



