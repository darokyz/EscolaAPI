from django.http import JsonResponse

# Create your views here.

def estudantes (request):

    if request.method == 'GET':
        estudantes = {
            'id': 1,
            'Nome': 'Lais'
        }
    return JsonResponse(estudantes)