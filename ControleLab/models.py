from django.db import models
import datetime

# Create your models here.

class Laboratorio(models.Model):
    patrimonio = models.CharField(max_length=8)
    local = models.CharField(max_length=120)

class Computador(models.Model):

    STATUS = [
        ('Dísponivel', 'Dísponivel'),
        ('Indísponivel', 'Indísponivel'),
        ('Em Manutenção', 'Em Manutenção')
    ]

    patrimonio = models.CharField(max_length=8)
    numero = models.CharField(max_length=2, default='0')
    status = models.CharField(max_length=13, choices=STATUS)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)

class Relatorio(models.Model):

    SIM_NAO = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    data = models.CharField(max_length=12, default=datetime.date.today())
    numero = models.ForeignKey(Computador, on_delete=models.CASCADE)
    observacao = models.CharField(max_length=550, default='S/O')
    carregador = models.CharField(max_length=4, choices=SIM_NAO)
    horario_emprestimo = models.CharField(max_length=10, default='--:--')
    horario_devolucao = models.CharField(max_length=10, default='--:--')
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.solicitante} - {self.data}"
    