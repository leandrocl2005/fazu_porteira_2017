from django.contrib import admin
from .models import Aluno, Projeto, Avaliador, Avaliacao, Cadastro

# Register your models here.
admin.site.register(Projeto)
admin.site.register(Aluno)
admin.site.register(Avaliador)
admin.site.register(Avaliacao)
admin.site.register(Cadastro)