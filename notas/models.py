from django.db import models

class Pais(models.Model):
  class Meta:
    verbose_name_plural = "paises"
  nombre = models.CharField(max_length=100)
  codigo = models.IntegerField()

  def __str__(self):
    return self.nombre