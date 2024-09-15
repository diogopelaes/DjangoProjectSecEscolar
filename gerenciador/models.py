# gerenciador/models.py
from django.db import models
from django.core.exceptions import ValidationError


class Aluno(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.matricula} - {self.nome}"

class Turma(models.Model):
    numero = models.PositiveSmallIntegerField(null=False, blank=False)
    letra = models.CharField(max_length=1, null=False, blank=False)
    ano = models.PositiveSmallIntegerField(null=False, blank=False)
    curso = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Turma {self.numero}{self.letra} - {self.curso} ({self.ano})"

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    disciplina = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.disciplina}"
