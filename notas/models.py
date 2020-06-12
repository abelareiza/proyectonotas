from django.db import models
from django.urls import reverse

class Pais(models.Model):
  class Meta:
    verbose_name_plural = "paises"
  nombre = models.CharField(max_length=100)
  codigo = models.IntegerField(primary_key=True)

  def __str__(self):
    return self.nombre

  def get_absolute_url(self):
    return reverse('pais-detail', kwargs={'pk' : self.pk})