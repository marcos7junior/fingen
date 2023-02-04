from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=300)

    def __str__(self):
        return self.nome_categoria

class Transacao(models.Model):
    titulo = models.CharField(max_length=200)
    receita = models.FloatField(Blank=False, null=False, default=0)
    despesa = models.FloatField(Blank=False, null=False, default=0)
    data = models.models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
