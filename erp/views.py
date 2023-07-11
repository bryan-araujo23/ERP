from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from erp.forms import FuncionarioForm, ProdutoForm
from .models import Funcionario, Produto


class HomeView(TemplateView):
    template_name = 'erp/index.html'



def cria_funcionario(requisicao: HttpRequest):
    if requisicao.method == 'GET':                 # Se variável.método GET
        form = FuncionarioForm()                   # var form = classe FuncionarioForm e seus campos de formulário forms.py
        return render(requisicao, template_name='erp/funcionarios/novo.html', context={"form": form})


    elif requisicao.method == 'POST':               # Envia dados
        form = FuncionarioForm(requisicao.POST)     # envia todos os dados do formulário preenchido

        if form.is_valid():                         # se meu formulário e seus campos foram preenchido corretamente.
                                                    # var funcionario = classe Funcionario de models.py

            funcionario = Funcionario(

                nome=form.cleaned_data.get('nome'),
                sobrenome=form.cleaned_data.get('sobrenome'),
                cpf=form.cleaned_data.get('cpf'),
                email_funcional=form.cleaned_data.get('email_funcional'),
                remuneracao=form.cleaned_data.get('remuneracao'),
            )
             # o Django armazena os dados válidos no dicionário cleaned_data

            funcionario.save()

            return HttpResponseRedirect(redirect_to='/') # barra quer dizer que voltamos para raiz da app




def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(requisicao, template_name='erp/funcionarios/list.html',  context={"funcionarios": funcionarios})

def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):    # 1
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)

        except Funcionario.DoesNotExist:
            funcionario = None

        return render(requisicao, template_name='erp/funcionarios/detalhe.html', context={"funcionario": funcionario})

    
def atualiza_funcionario(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(instance=funcionario)

        return render(requisicao, template_name='erp/funcionarios/atualiza.html', context={"form": form})

    elif requisicao.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(requisicao.POST, instance=funcionario)
         # fomulario atualizado com a chave cadastrada anteriormente

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}') # retornou para url detalhe


class ProdutoCreateView(CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')
#            nome do app em urls.py:nome da view
