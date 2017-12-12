from django import forms

from .models import Avaliacao, Cadastro

class AvaliacaoForm(forms.ModelForm):

    class Meta:
        model = Avaliacao
        fields = ('nota','estrelas','ocorrencias',)

class CadastroForm(forms.ModelForm):

	class Meta:
		model = Cadastro
		fields = ('nome', 'email', 'telefone',)

