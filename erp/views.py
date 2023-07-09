#  Camada view:
#  Prover o roteamento de rotas,
#  Processar Requisições HTTP,
#  Aplicar as regras de negócio definidas para cada view
#  Formular Respostas HTTP, Recepcionar requisições http, Processa - lás e responde -  las

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from erp.forms import FuncionarioForm
from .models import Funcionario



def home(requisicao: HttpRequest):  # pycharm não entende o que é a requisição, seu tipo primitivo. Por isso usamos type hint
    if requisicao.method == 'GET':  # Vamos verificar qual método http, dependendo do método, teremos um tipo de processamento
        return render(requisicao, template_name='erp/index.html')


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