from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):


    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)  # Verifica aqui se esta fazendo uma submissão de dados ao servidor,
    # e caso não estiver passamos o None

    # Verificamos aqui se o formulário é valido ou não
    # Se for válido pegamos os seus campos e printamos no console
    if str(request.method) == 'POST':
        print(f'POST: {request.POST}')
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Formulário enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar formulário')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':

        print(f'Usuário:{request.user}')
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST,
                                    request.FILES)  # Aqui pegamos o metodo post e um arquivo, que no nosso
            # caso é a imagem do produto
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
