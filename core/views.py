from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Projeto, Avaliador, Avaliacao, Cadastro
from .forms import AvaliacaoForm, CadastroForm

# Create your views here.
def home(request):
	context = {'user':"Leandro"}
	return render(request, 'home.html', context)

def login(request):
	return render(request, 'login.html')

def cadastro_avaliador(request):
	cadastro = Cadastro()
	if request.method == "POST":
		form = CadastroForm(request.POST, instance=cadastro)
		if form.is_valid():
			cadastro = form.save(commit=False)
			cadastro.save()
			return redirect('cadastro_sucesso')
	else:
		print("merda")
		form = CadastroForm(instance=cadastro)
	return render(request, 'cadastro_avaliador.html', {'form':form})

def cadastro_sucesso(request):
	return render(request, 'cadastro_sucesso.html')


@login_required
def projetos_list(request):
	projetos = Projeto.objects.filter(avaliador__user__id = request.user.id)
	return render(request, 'projetos_list.html', {'projetos':projetos})

@login_required
def projeto_avaliar(request, pk):
	projeto = get_object_or_404(Projeto, pk=pk)
	avaliador = Avaliador.objects.filter(user__id=request.user.id)[0]
	avaliacoes =Avaliacao.objects.filter(avaliador__user__id=request.user.id).filter(projeto__pk=pk)
	try:
		avaliacao = avaliacoes[0]
		nota = avaliacao.nota
		estrelas = avaliacao.estrelas
		ocorrencias = avaliacao.ocorrencias
	except:
		avaliacao = Avaliacao()
		avaliacao.projeto = projeto
		avaliacao.avaliador = avaliador
		nota = 0
		estrelas = 0
		ocorrencias = " "
	avaliacao.nota = nota
	avaliacao.estrelas = estrelas
	avaliacao.save()
	context = {
		'avaliacao': avaliacao,
		'projeto': projeto,
		'avaliador': avaliador,
		'nota': nota,
		'estrelas': estrelas,
		'ocorrencias': ocorrencias,
	}
	return render(request, 'projeto_avaliar.html', context)

@login_required
def projeto_detalhe(request, pk):
	projeto = get_object_or_404(Projeto, pk=pk)
	pk_projeto = pk
	avaliador = Avaliador.objects.filter(user__id=request.user.id)[0]
	context = {
		'projeto': projeto,
		'avaliador': avaliador,
		'pk_projeto': pk_projeto,
	}
	return render(request, 'projeto_detalhe.html', context)

@login_required
def nova_avaliacao(request, pk):
	avaliacao = get_object_or_404(Avaliacao, pk=pk)

	if request.method == "POST":
		form = AvaliacaoForm(request.POST, instance=avaliacao)
		if form.is_valid():
			avaliacao = form.save(commit=False)
			avaliacao.save()
			return redirect('projetos_list')
	else:
		print("merda")
		form = AvaliacaoForm(instance=avaliacao)
	return render(request, 'projeto_nova_avaliacao.html',{'form':form})
