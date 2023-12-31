from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from erp.forms import FuncionarioForm, ProdutoForm
from .models import Funcionario, Produto, Venda

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ErpLoginView(LoginView):             # antiPenúltima clase para ser criada, pagina inicial da aplicação
    template_name = 'erp/login.html'       # Home página principal da parte privada de quem tem acesso
    success_url = reverse_lazy('erp:dashboard')
    redirect_authenticated_user = True     # Usuários que estão autenticado serão redirirecionado a success_url

class ErpLogoutView(LogoutView):
    template_name = 'erp/logout.html'


class DashboardView(LoginRequiredMixin, TemplateView):      # penúltima clase para ser criada, vá para settings.py e crie 2 const: LOGIN_URL e LOGIN_REDIRECT_URL
    template_name = 'erp/dashboard.html'


class HomeView(TemplateView):
    template_name = 'erp/index.html'

@login_required                     # autenticação última aula  camada view
def cria_funcionario(requisicao: HttpRequest):
    if requisicao.method == 'GET':  # Se variável.método GET
        form = FuncionarioForm()  # var form = classe FuncionarioForm e seus campos de formulário forms.py
        return render(requisicao, template_name='erp/funcionarios/novo.html', context={"form": form})


    elif requisicao.method == 'POST':  # Envia dados
        form = FuncionarioForm(requisicao.POST)  # envia todos os dados do formulário preenchido

        if form.is_valid():  # se meu formulário e seus campos foram preenchido corretamente.
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

            return HttpResponseRedirect(redirect_to='/')  # barra quer dizer que voltamos para raiz da app

@login_required
def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(requisicao, template_name='erp/funcionarios/lista.html', context={"funcionarios": funcionarios})

@login_required
def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):  # 1
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)

        except Funcionario.DoesNotExist:
            funcionario = None

        return render(requisicao, template_name='erp/funcionarios/detalhe.html', context={"funcionario": funcionario})



@login_required
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

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')  # retornou para url detalhe


class ProdutoCreateView(LoginRequiredMixin, CreateView):   # Sempre colocar Mixin como primeiro parâmetro
    model = Produto
    template_name = 'erp/produtos/novo.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')
#            nome do app em urls.py:nome da view


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'erp/produtos/list.html'
    context_object_name = 'produtos' # objeto que será passado para o template


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'erp/produtos/atualiza.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produto'        # variável de contexto que podemos manipular no template


    def get_object(self, queryset=None):
        """ Método responsável por obter um objeto específico
            do modelo Produto a partir de um conjunto de dados. """

        # Tenta executar o seguinte código:
        try:
            # Chama o método get_object() da superclasse (DetailView) usando a função super().
            return super().get_object(queryset)
            # Isso executa a lógica padrão de obtenção do objeto e retorna o objeto encontrado.

        # Se ocorrer uma exceção Http404 (página não encontrada), entra nesse bloco:
        except Http404:
            return None
            # Retorna None, indicando que nenhum objeto foi encontrado.



class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:lista_produtos')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)

        except Http404:
            return None


class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:home')
    fields = ['funcionario', 'produto']


class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'



class VendaDetailView(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)

        except Http404:
            return None


class VendaUpdateView(LoginRequiredMixin,  UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = '__all__'
    success_url = reverse_lazy('erp:lista_vendas')

class VendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)

        except Http404:
            return None