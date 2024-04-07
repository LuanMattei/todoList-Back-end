from django.db import models

class Card(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    status = models.IntegerField()
    
    def __str__(self):
        return super().__str__()