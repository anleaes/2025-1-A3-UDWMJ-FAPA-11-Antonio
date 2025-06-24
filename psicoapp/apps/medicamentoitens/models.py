from django.db import models
from apps.medicamentos.models import Medicamento
from apps.prescricoes.models import Prescricao

# Create your models here.

class MedicamentoItem(models.Model):
    prescricao = models.ForeignKey(Prescricao, on_delete=models.CASCADE, related_name='itens')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.medicamento.nome} - Prescrição {self.prescricao.id}"