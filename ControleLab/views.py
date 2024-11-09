from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ControleLab.models import *
import datetime as dt
from django.shortcuts import get_object_or_404

# Create your views here.

def acesso(request):
    error_message = None

    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(request, username=nome, password=senha)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Usuário ou senha inválidos.'

    return render(request, 'acesso.html', {'error_message': error_message})

@login_required
def index(request):

    laboratorios = Laboratorio.objects.all()
    relatorios = Relatorio.objects.all()

    return render(request, 'index.html', {'laboratorios':laboratorios, 'relatorios': relatorios})

@login_required
def adicionar_lab(request):

    if request.method == 'POST':
        patrimonio = request.POST.get('patrimonio')
        local = request.POST.get('local')

        laboratorio = Laboratorio(patrimonio=patrimonio, local=local)
        laboratorio.save()

        return redirect('index')

    return render(request, 'adicionar_lab.html')

@login_required
def computadores(request, id):



    computadores_info = Computador.objects.filter(laboratorio_id=id)
    laboratorio = Laboratorio.objects.get(id=id)

    return render(request, 'computadores.html', {'computadores_info':computadores_info, 'laboratorio':laboratorio})

@login_required
def alterar_status_comp(request, id):
    computador = Computador.objects.get(id=id)

    status_comp =  computador.status

    if status_comp == 'Dísponivel':
        computador.status = 'Indísponivel'
    elif status_comp == 'Indísponivel':
        computador.status = 'Em Manutenção'
    else:
        computador.status = 'Dísponivel'
    computador.save()

    return redirect('computadores', id=computador.laboratorio.id)

@login_required
def adicionar_comp(request, id):

    laboratorio = Laboratorio.objects.get(id=id)

    if request.method == 'POST':
        patrimonio = request.POST.get('patrimonio')
        numero = request.POST.get('numero')
        status = request.POST.get('status')

        computador = Computador(numero=numero, patrimonio=patrimonio, status=status, laboratorio_id=laboratorio.id)
        computador.save()

        return redirect('index')

    return render(request, 'adicionar_comp.html', {'laboratorio':laboratorio})

@login_required
def excluir_comp(request, id):

    computador = Computador.objects.get(id=id)
    computador.delete()

    return redirect('computadores', id=computador.laboratorio.id)

@login_required
def relatorio(request):
    
    relatorios = Relatorio.objects.all()

    return render(request, 'relatorio.html', {'relatorios': relatorios})

@login_required
def criar_relatorio(request, id):
    laboratorio = Laboratorio.objects.get(id=id)

    if request.method == 'POST':
        responsavel = request.POST.get('responsavel')
        patrimonio = request.POST.get('numero')
        carregador = request.POST.get('carregador')

        computador = Computador.objects.get(patrimonio=patrimonio)

        d = dt.date.today()

        if computador.status == 'Dísponivel':
            relatorio = Relatorio(
                responsavel=responsavel,
                numero=computador,
                carregador=carregador,
                data=d.strftime("%d/%m/%Y"),
                horario_emprestimo=dt.datetime.now().strftime("%I:%M")
            )
            relatorio.save()

            # Atualizar o status do computador para 'Indísponivel'
            computador.status = 'Indísponivel'
            computador.save()

            return redirect('computadores', id=laboratorio.id)
        
    return render(request, 'criar_relatorio.html', {'laboratorio': laboratorio})

@login_required
def devolver_comp(request, id):
    if request.method == 'POST':

        observacao = request.POST.get('observacao')
        relatorio_id = request.POST.get('relatorio_id')

        relatorio = get_object_or_404(Relatorio, id=relatorio_id)

        relatorio.observacao = observacao
        relatorio.horario_devolucao = dt.datetime.now().strftime("%I:%M")
        relatorio.save()

        computador = get_object_or_404(Computador, id=relatorio.numero.id)
        computador.status = 'Disponível'
        computador.save()

        return redirect('relatorio')
    
    return redirect('relatorio')

@login_required
def sair(request):
    logout(request)
    return redirect('acesso')