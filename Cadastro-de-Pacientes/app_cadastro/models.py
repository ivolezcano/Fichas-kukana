from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    profissao = models.TextField(max_length=255)
    nascimento = models.DateField()
    plano_saude = models.TextField(max_length=255)
    diagnostico = models.TextField(max_length=255)