# gerenciador/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.fazer_logout, name='logout'),
    path('aluno/cadastro/', views.form_aluno, name='form_aluno'),
    path('professor/cadastro/', views.form_professor, name='form_professor'),
    path('turma/cadastro/', views.form_turma, name='form_turma'),
]