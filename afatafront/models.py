from django.db import models

class lideranca(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])
    estado_civil = models.CharField(max_length=20, choices=[('solteiro', 'Solteiro(a)'), ('casado', 'Casado(a)'), ('divorciado', 'Divorciado(a)'), ('viuvo', 'Viúvo(a)')])
    endereco = models.CharField(max_length=200)
    regiao_atuante = models.CharField(max_length=100)
    assessor_coordenador = models.CharField(max_length=100)
    informacoes_gerais = models.TextField()

def __str__(self):
    return self.nome


class AssociacaoParceira(models.Model):
    instituicao = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    regiao_atuante = models.CharField(max_length=100)
    informacoes_gerais = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.instituicao
