import os
import django

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secretaria_escolar.settings')
django.setup()

from gerenciador.models import Turma

# Função para criar turmas
def criar_turmas():
    numeros = [1, 2, 3]
    letras = ['A', 'B', 'C']
    ano = 2025
    curso = "Ensino Médio"
    
    for numero in numeros:
        for letra in letras:
            Turma.objects.create(
                numero=numero,
                letra=letra,
                ano=ano,
                curso=curso
            )
            print(f'Turma {numero}{letra} criada com sucesso!')

# Cria 9 turmas
if __name__ == '__main__':
    criar_turmas()