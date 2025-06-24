
from django.db import models
from apps.pacientes.models import Paciente
from apps.profissionais.models import Profissional

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente.nome} com {self.profissional.nome} em {self.data}"
