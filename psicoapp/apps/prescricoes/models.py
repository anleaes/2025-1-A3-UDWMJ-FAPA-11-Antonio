from django.db import models
from apps.atendimentos.models import Atendimento

# Create your models here.

class Prescricao(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return f"Prescrição do atendimento em {self.atendimento.data}"
