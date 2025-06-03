from django.db import models

# Create your models here.
class Especialidade(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)
    
    def getNome(self):
        return self.nome
        
    def setNome(self, nome):
        self.nome = nome
        self.save()
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        ordering = ['nome']

    def __str__(self):
        return self.nome
