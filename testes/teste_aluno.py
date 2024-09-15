import os
import django
from random import randint
from faker import Faker

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secretaria_escolar.settings')
django.setup()

from gerenciador.models import Aluno

# Gerador de dados falsos
fake = Faker('pt_BR')

# Função para criar alunos
def criar_alunos(quantidade):
    for _ in range(quantidade):
        nome = fake.name()
        idade = randint(6, 18)
        matricula = fake.unique.random_number(digits=6)
        Aluno.objects.create(nome=nome, idade=idade, matricula=matricula)
        print(f'Aluno {nome} criado com sucesso!')

# Cria 20 alunos
if __name__ == '__main__':
    criar_alunos(20)