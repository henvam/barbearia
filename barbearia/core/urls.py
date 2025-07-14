from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', views.novo_agendamento, name='novo_agendamento'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agendamentos/concluir/<int:agendamento_id>/', views.concluir_agendamento, name='concluir_agendamento'),
    path('agendamentos/excluir/<int:agendamento_id>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('agendamentos/editar/<int:agendamento_id>/', views.editar_agendamento, name='editar_agendamento'),
    path('calendario/', views.calendario_agendamentos, name='calendario_agendamentos'),
    path('calendario/eventos/', views.eventos_agendamentos, name='eventos_agendamentos'),
    path('agendamento-online/', views.agendamento_publico, name='agendamento_publico'),

]
