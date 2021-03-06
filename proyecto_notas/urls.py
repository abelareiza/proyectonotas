"""proyecto_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from notas import views as notas_views
from notas.views import (
    PaisListView,
    PaisDetailView,
    PaisCreateView,
    PaisUpdateView,
    PaisDeleteView
)

urlpatterns = [
    path('', PaisListView.as_view(), name='notas-home'),
    path('pais/<int:pk>/', PaisDetailView.as_view(), name='pais-detail'),
    path('pais/new/', PaisCreateView.as_view(), name='pais-create'),
    path('pais/<int:pk>/update', PaisUpdateView.as_view(), name='pais-update'),
    path('pais/<int:pk>/delete', PaisDeleteView.as_view(), name='pais-delete'),

    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('action_confirm/', notas_views.action_confirm, name='action-confirm'),

]
