from django.db import models

# Create your models here.
class Evento(models.Model):
    codigo_evento = models.AutoField(primary_key=True)
    nome = models.CharField(null=False, blank=False)
    lotacao = models.IntegerField(null=True, blank=True)
    dia = models.DateField(null=False, blank=False)
    horario = models.TimeField(null=False, blank=False)
    ingresso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(null=False, blank=False)

    def __str__(self):
        return self.nome