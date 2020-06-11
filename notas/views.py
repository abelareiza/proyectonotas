from django.shortcuts import render, redirect
from .models import Pais

def home(request):
  context = {
    'paises': Pais.objects.all()
  }
  if request.user.is_authenticated:
    return render(request, 'notas/home.html', context)
  else:
    return redirect('login')