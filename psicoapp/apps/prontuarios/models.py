from django.db import models
from apps.pacientes.models import Paciente
from apps.prescricoes.models import Prescricao

# Create your models here.

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios')
    observacoes = models.TextField()
    prescricoes = models.ManyToManyField(Prescricao, related_name='prontuarios', blank=True)

    def __str__(self):
        return f'Prontuário de {self.paciente.nome}'
