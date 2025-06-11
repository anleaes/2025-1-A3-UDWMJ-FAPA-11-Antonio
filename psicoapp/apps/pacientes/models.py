from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()

    def addHistorico(self):
        pass  # lógica será definida depois

    def getHistorico(self):
        pass  # lógica será definida depois

    def __str__(self):
        return self.nome