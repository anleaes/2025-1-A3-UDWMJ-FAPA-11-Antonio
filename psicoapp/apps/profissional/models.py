from django.db import models
from especialidades.models import Especialidade  

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

class ProfissionalEspecialidade(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    registro_conselho = models.CharField(max_length=50)

    class Meta:
        unique_together = ('profissional', 'especialidade')