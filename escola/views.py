from django.shortcuts import JsonResponse 

# Create your views here.

def alunos(request):
    if request.method == 'GET':
        aluno = {'id':1, 'nome': 'Guilherme' }
        return JsonResponse(aluno)

