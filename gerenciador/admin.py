# gerenciador/admin.py
from django.contrib import admin
from .models import Aluno, Turma, Professor

admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Professor)

