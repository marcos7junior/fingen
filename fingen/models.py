from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=300)

    def __str__(self):
        return self.nome_categoria

class Transacao(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.FloatField(blank=False, null=False, default=0)
    receita = models.BooleanField(default=False)
    recorrente = models.BooleanField(default=False)
    meses = models.IntegerField(default=1, blank=False, null=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
