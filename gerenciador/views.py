# gerenciador/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gerenciador.models import Aluno, Professor, Turma


def index(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'alerta': 'Usuário ou senha incorreta'
            }
            return render(request, 'index.html', context)
        else:
            login(request, user)
    return render(request, 'index.html')


def fazer_logout(request):
    logout(request)
    return redirect('index')


@login_required
def form_aluno(request):
    if request.method == 'POST':
        # Extrair dados do formulário
        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        ativo = request.POST.get('ativo') == 'on'

        # Criar novo aluno
        aluno = Aluno(
            matricula=matricula,
            nome=nome,
            cpf=cpf,
            ativo=ativo
        )

        # Verificar e adicionar telefone se não estiver vazio
        if telefone:
            aluno.telefone = telefone

        # Verificar e adicionar data de nascimento se não estiver vazia
        if data_nascimento:
            aluno.data_nascimento = data_nascimento

        # Salvar o aluno
        aluno.save()
        context = {
            'alerta': f'Aluno {aluno} cadastrado com sucesso'
        }

        # Redirecionar para uma página de sucesso ou lista de alunos
        return redirect('index')  # Você precisará criar esta view e URL

    # Se for GET, apenas renderiza o formulário
    return render(request, 'form_aluno.html')


@login_required
def form_professor(request):
    if request.method == 'POST':
        # Extrair dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        disciplina = request.POST.get('disciplina')
        ativo = request.POST.get('ativo') == 'on'

        # Criar novo professor
        professor = Professor(
            nome=nome,
            cpf=cpf,
            email=email,
            disciplina=disciplina,
            ativo=ativo
        )

        # Verificar e adicionar telefone se não estiver vazio
        if telefone:
            professor.telefone = telefone

        # Verificar e adicionar data de nascimento se não estiver vazia
        if data_nascimento:
            professor.data_nascimento = data_nascimento

        # Salvar o professor
        professor.save()
        context = {
            'alerta': f'Professor {professor} cadastrado com sucesso'
        }

        # Redirecionar para uma página de sucesso ou lista de professores
        return redirect('index')  # Você precisará criar esta view e URL

    # Se for GET, apenas renderiza o formulário
    return render(request, 'form_professor.html')


@login_required
def form_turma(request):
    if request.method == 'POST':
        # Extrair dados do formulário
        numero = request.POST.get('numero')
        letra = request.POST.get('letra')
        ano = request.POST.get('ano')
        curso = request.POST.get('curso')

        # Criar nova turma
        turma = Turma(
            numero=numero,
            letra=letra,
            ano=ano,
            curso=curso
        )

        # Salvar a turma
        turma.save()
        context = {
            'alerta': f'Turma {turma} cadastrada com sucesso'
        }

        # Redirecionar para uma página de sucesso ou lista de turmas
        return redirect('index')  # Você precisará criar esta view e URL

    # Se for GET, apenas renderiza o formulário
    return render(request, 'form_turma.html')


@login_required
def lista_alunos(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos
    }
    return render(request, 'alunos.html', context)


@login_required
def lista_professores(request):
    professores = Professor.objects.all()
    context = {
        'professores': professores
    }
    return render(request, 'professores.html', context)


@login_required
def lista_turmas(request):
    turmas = Turma.objects.all()
    context = {
        'turmas': turmas
    }
    return render(request, 'turmas.html', context)
