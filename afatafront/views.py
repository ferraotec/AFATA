from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import lideranca, AssociacaoParceira  # Importar os modelos
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def pagina1(request):
    return render(request, 'login.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('pagina2')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('pagina2')
        else:
            messages.error(request, 'Nome de usuário ou senha inválido.')
            return render(request, 'login.html', {'error_message': 'Nome de usuário ou senha inválido.'})
    
    return render(request, 'login.html')

@login_required  # Aqui você usa o decorador
def pagina2(request):
    return render(request, 'modulos.html')

def custom_logout(request):
    logout(request)
    # Redirecione para a página de login personalizada
    return redirect('pagina1')  # Substitua 'pagina1' pela URL da sua página de login



def cadastro_lideranca(request):
    return render(request, 'cadastro_lideranca.html')   

def pagina_de_sucesso(request):
    return render(request, 'pagina_de_sucesso.html')

def processar_cadastro_lideranca(request):
    if request.method == 'POST':
        # Recupere os dados do formulário enviado pelo POST
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        estado_civil = request.POST.get('estado_civil')
        endereco = request.POST.get('endereco')
        regiao_atuante = request.POST.get('regiao_atuante')
        assessor_coordenador = request.POST.get('assessor_coordenador')
        informacoes_gerais = request.POST.get('informacoes_gerais')

        # Salve os dados do formulário no banco de dados usando o modelo lideranca
        lideranca.objects.create(
            nome=nome,
            data_nascimento=data_nascimento,
            sexo=sexo,
            estado_civil=estado_civil,
            endereco=endereco,
            regiao_atuante=regiao_atuante,
            assessor_coordenador=assessor_coordenador,
            informacoes_gerais=informacoes_gerais
        )
   # Redirecione para a página de sucesso ou qualquer outra página desejada
        return JsonResponse({'success': True, 'lideranca_id': lideranca.id})
    # Se o método da requisição não for POST, renderize a página de cadastro
    return render(request, 'cadastro_lideranca.html')

def dashboard_data(request):
    # Recupere todos os objetos da tabela lideranca
    liderancas = list(lideranca.objects.all().values())
    return JsonResponse({'liderancas': liderancas})


def associacoes_parceiras(request):
    return render(request, 'associacoes_parceiras.html') 

def processar_cadastro_associacoes_parceiras(request):
    if request.method == 'POST':
        # Recupere os dados do formulário enviado pelo POST
        instituicao = request.POST.get('instituicao')
        responsavel = request.POST.get('responsavel')
        contato = request.POST.get('contato')
        endereco = request.POST.get('endereco')
        regiao_atuante = request.POST.get('regiao_atuante')
        informacoes_gerais = request.POST.get('informacoes_gerais')

        # Salve os dados do formulário no banco de dados usando o modelo AssociacaoParceira
        associacao = AssociacaoParceira.objects.create(
            instituicao=instituicao,
            responsavel=responsavel,
            contato=contato,
            endereco=endereco,
            regiao_atuante=regiao_atuante,
            informacoes_gerais=informacoes_gerais
        )

        # Redirecione para a página de sucesso ou qualquer outra página desejada
        return JsonResponse({'success': True, 'associacao_id': associacao.id})

    # Se o método da requisição não for POST, renderize a página de cadastro
    return render(request, 'cadastro_associacoes_parceiras.html')

def dashboard_associacao(request):
    # Recupere todos os objetos da tabela AssociacaoParceira
    assoc_parceiras = list(AssociacaoParceira.objects.all().values())
    return JsonResponse({'assoc_parceiras': assoc_parceiras})