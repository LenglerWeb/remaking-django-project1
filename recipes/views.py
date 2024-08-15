from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME em "/RECIPES/VIEWS/"')


def sobre(request):
    return HttpResponse('SOBRE em "/RECIPES/VIEWS/"')


def contato(request):
    return HttpResponse('CONTATO em "/RECIPES/VIEWS/"')
