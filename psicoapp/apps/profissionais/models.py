from django.db import models

# Create your models here.

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def agendarAtendimento(self):
        return f"Agendamento criado para o profissional {self.nome}"

    def getAgenda(self):
        return f"Agenda do profissional {self.nome}"

    def __str__(self):
        return self.nome
