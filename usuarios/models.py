from django.db import models

from django.contrib.auth.models import User

class Usuario(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  esta_activo = models.BooleanField(default=True)
  
  def __str__(self):
    return self.user.username