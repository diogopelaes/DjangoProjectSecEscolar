import os
import django
from faker import Faker

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secretaria_escolar.settings')
django.setup()

from gerenciador.models import Professor

# Gerador de dados falsos
fake = Faker('pt_BR')

# Função para criar professores
def criar_professores(quantidade):
    for _ in range(quantidade):
        nome = fake.name()
        cpf = fake.unique.cpf()
        telefone = fake.phone_number()
        data_nascimento = fake.date_of_birth(minimum_age=25, maximum_age=65)
        email = fake.unique.email()
        disciplina = fake.job()
        Professor.objects.create(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            data_nascimento=data_nascimento,
            email=email,
            disciplina=disciplina,
            ativo=True
        )
        print(f'Professor {nome} criado com sucesso!')

# Cria 15 professores
if __name__ == '__main__':
    criar_professores(15)