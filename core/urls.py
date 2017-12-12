from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {
    	'template_name': 'login.html'
    	}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^projetos/lista/$', views.projetos_list, name='projetos_list'),
    url(r'^projeto/avaliar/(?P<pk>\d+)/$', views.projeto_avaliar, name='projeto_avaliar'),
    url(r'^projeto/detalhe/(?P<pk>\d+)/$', views.projeto_detalhe, name='projeto_detalhe'),
    url(r'^projeto/nova_avaliacao/(?P<pk>\d+)/$', views.nova_avaliacao, name='nova_avaliacao'),
    url(r'^cadastro_avaliador/$', views.cadastro_avaliador, name='cadastro_avaliador'),
    url(r'^cadastro_sucesso/$',views.cadastro_sucesso, name='cadastro_sucesso'),
]