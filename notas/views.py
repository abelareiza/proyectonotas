from django.shortcuts import render
from .models import Pais

def home(request):
  context = {
    'paises': Pais.objects.all()
  }
  return render(request, 'notas/home.html', context)