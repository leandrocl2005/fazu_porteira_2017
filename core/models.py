from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
	nome = models.CharField("Nome", max_length=120)
	matricula = models.CharField("Matricula", max_length=9)

	def __str__(self):              
		return self.nome

class Projeto(models.Model):
	nome = models.CharField("Nome", max_length=120)
	resumo = models.TextField("Resumo", blank=True, null=True)
	aluno = models.ManyToManyField("Aluno")
	avaliador = models.ManyToManyField("Avaliador")

	def __str__(self):              
		return self.nome

class Avaliador(models.Model):
	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		related_name = 'avaliador')

	def __str__(self):              
		return self.user.username

class Avaliacao(models.Model):

	projeto = models.ForeignKey(Projeto,blank=True,null=True)
	avaliador = models.ForeignKey(Avaliador,blank=True,null=True)
	estrelas = models.PositiveIntegerField("Estrelas",blank=True,null=True)
	nota = models.PositiveIntegerField("Nota", blank=True, null=True)
	ocorrencias = models.TextField("Ocorrências", blank=True, null=True)

	def __str__(self):              
		return self.projeto.nome.upper() + " (avaliado por " + self.avaliador.user.username + ")"

class Cadastro(models.Model):

	nome = models.CharField("Nome", max_length=120)
	email = models.EmailField("E-mail", max_length=120)
	telefone = models.CharField("Telefone", max_length=15)

	def __str__(self):              
		return self.nome