from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)
from .models import Pais

class PaisListView(ListView):
  model = Pais
  template_name = 'notas/home.html'
  context_object_name = 'paises'
  ordering = ['codigo']

class PaisDetailView(DetailView):
  model = Pais

class PaisCreateView(LoginRequiredMixin, CreateView):
  model = Pais
  fields = ['nombre', 'codigo']

class PaisUpdateView(LoginRequiredMixin, UpdateView):
  model = Pais
  fields = ['nombre', 'codigo']

class PaisDeleteView(LoginRequiredMixin, DeleteView):
  model = Pais
  success_url = '/'