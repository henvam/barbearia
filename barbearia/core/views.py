from django.shortcuts import render, redirect
from .models import Cliente, Agendamento
from .forms import ClienteForm, AgendamentoForm  # <- IMPORTANTE!

def home(request):
    return render(request, 'home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.select_related('cliente', 'servico').order_by('data', 'hora')
    return render(request, 'agendamentos.html', {'agendamentos': agendamentos})

def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'novo_agendamento.html', {'form': form})

from django.db.models import Count, Sum
from django.utils import timezone

def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_agendamentos = Agendamento.objects.count()
    agendamentos_concluidos = Agendamento.objects.filter(concluido=True).count()
    valor_total = Agendamento.objects.filter(servico__isnull=False).aggregate(Sum('servico__preco'))['servico__preco__sum'] or 0

    contexto = {
        'total_clientes': total_clientes,
        'total_agendamentos': total_agendamentos,
        'agendamentos_concluidos': agendamentos_concluidos,
        'valor_total': valor_total,
    }

    return render(request, 'dashboard.html', contexto)

from django.shortcuts import get_object_or_404

def concluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    agendamento.concluido = True
    agendamento.save()
    return redirect('lista_agendamentos')

def excluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('lista_agendamentos')
    return render(request, 'confirmar_exclusao.html', {'agendamento': agendamento})
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'editar_agendamento.html', {'form': form, 'agendamento': agendamento})

from django.http import JsonResponse

def eventos_agendamentos(request):
    agendamentos = Agendamento.objects.select_related('cliente', 'servico')

    eventos = []
    for ag in agendamentos:
        eventos.append({
            'title': f'{ag.cliente.nome} - {ag.servico.nome}',
            'start': f'{ag.data}T{ag.hora}',
            'end': f'{ag.data}T{ag.hora}',
            'color': '#28a745' if ag.concluido else '#dc3545',
        })

    return JsonResponse(eventos, safe=False)

from django.shortcuts import render

def calendario_agendamentos(request):
    return render(request, 'calendario.html')
from .forms_externo import AgendamentoPublicoForm

def agendamento_publico(request):
    if request.method == 'POST':
        form = AgendamentoPublicoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'agendamento_sucesso.html')
    else:
        form = AgendamentoPublicoForm()
    return render(request, 'agendamento_publico.html', {'form': form})
