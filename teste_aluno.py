import os
import django
from random import randint
from faker import Faker

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secretaria_escolar.settings')
django.setup()

from gerenciador.models import Aluno, Turma

# Gerador de dados falsos
fake = Faker('pt_BR')

# Função para criar turmas
def criar_turmas(quantidade):
    turmas = []
    for _ in range(quantidade):
        numero = randint(1, 3)
        letra = fake.random_element(elements=('A', 'B', 'C'))
        ano = randint(2020, 2023)
        curso = fake.word().capitalize()
        turma = Turma.objects.create(numero=numero, letra=letra, ano=ano, curso=curso)
        turmas.append(turma)
        print(f'Turma {numero}{letra} criada com sucesso!')
    return turmas

# Função para criar alunos
def criar_alunos(quantidade, turmas):
    for _ in range(quantidade):
        nome = fake.name()
        cpf = fake.unique.cpf()
        telefone = fake.phone_number()
        data_nascimento = fake.date_of_birth(minimum_age=6, maximum_age=18)
        matricula = fake.unique.random_number(digits=6)
        turma = fake.random_element(elements=turmas)
        Aluno.objects.create(
            matricula=matricula,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            data_nascimento=data_nascimento,
            ativo=True
        )
        print(f'Aluno {nome} criado com sucesso!')

# Cria 3 turmas e 20 alunos
if __name__ == '__main__':
    turmas = criar_turmas(3)
    criar_alunos(20, turmas)