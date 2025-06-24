from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, default='000000000')
    data_nasc = models.DateField()

    def addHistorico(self):
        pass  

    def getHistorico(self):
        pass  

    def __str__(self):
        return self.nome