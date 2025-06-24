from django.db import models
from apps.categorias.models import Categoria

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome