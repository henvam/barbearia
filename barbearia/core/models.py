from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao_minutos = models.IntegerField()

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data} {self.hora}"
