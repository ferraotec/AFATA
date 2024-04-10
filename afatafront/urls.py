from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import processar_cadastro_associacoes_parceiras

urlpatterns = [
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('', views.login_view, name='login'), 
    path('logout/', views.custom_logout, name='logout'),
    path('cadastro_lideranca/', views.cadastro_lideranca, name='cadastro_lideranca'),
    path('processar_cadastro_lideranca/', views.processar_cadastro_lideranca, name='processar_cadastro_lideranca'),
    path('pagina_de_sucesso/', views.pagina_de_sucesso, name='pagina_de_sucesso'),
    path('dashboard_data/', views.dashboard_data, name='dashboard_data'),
    path('associacoes_parceiras/', views.associacoes_parceiras, name='associacoes_parceiras'),
    path('processar_cadastro_associacoes_parceiras/', processar_cadastro_associacoes_parceiras, name='processar_cadastro_associacoes_parceiras'),
    path('dashboard_associacao/', views.dashboard_associacao, name='dashboard_associacao'),
]
