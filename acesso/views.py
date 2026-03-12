from django.shortcuts import render
from django.http import HttpResponse




def acesso_view(request):
    return render(request, 'acesso.html')