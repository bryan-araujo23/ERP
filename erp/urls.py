from core import settings
from django.conf.urls.static import static
from django.urls import path
from erp.views import cria_funcionario, lista_funcionarios, busca_funcionario_por_id, atualiza_funcionario, HomeView, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView, VendaCreateView,\
    VendaListView, VendaDetailView, VendaUpdateView, VendaDeleteView, ErpLoginView, DashboardView, ErpLogoutView

app_name = 'erp'

urlpatterns = [

    # Home
    path('', HomeView.as_view(), name='home'),

    #  Login e dashboard, as 2 últimas a serem criadas
    path('login/', ErpLoginView.as_view(), name='login'),
    path('logout/', ErpLogoutView.as_view(), name='logout'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Funcionários
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'), # 2º ordem de criação
    path('funcionarios/novo', cria_funcionario, name='cria_funcionario'), # 1º ordem de criação
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),# 3º ordem de criação
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'), # 4º ordem de criação



    # Produtos
    # .as_view()  que classe associada a ele deve ser tratada como uma view.
    path('produtos/', ProdutoListView.as_view(), name='lista_produtos'),       # 2º ordem de criação
    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto'),   # 1º ordem de criação
    path('produtos/atualiza/<pk>', ProdutoUpdateView.as_view(), name='atualiza_produto'), # 3º ordem de criação
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='detalhe_produto'),   # 4º ordem de criação
    path('produtos/deleta/<pk>', ProdutoDeleteView.as_view(), name='deleta_produto'),     # 5º ordem de criação


    # Vendas
    path('vendas/', VendaListView.as_view(), name='lista_vendas'),                  # 2º ordem de criação
    path('vendas/novo', VendaCreateView.as_view(), name='cria_venda'),              # 1º ordem de criação
    path('vendas/detalhe/<pk>', VendaDetailView.as_view(), name='detalhe_venda'),   # 3º ordem de criação
    path('vendas/atualiza/<pk>', VendaUpdateView.as_view(), name='atualiza_venda'), # 4º ordem de criação
    path('vendas/deleta/<pk>', VendaDeleteView.as_view(), name='deleta_venda'),     # 5º ordem de criação


]

# VERIFICAR em settings.py se debug está ativo; se sim, vamos adcionar aquela url de settings MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from core import settings - importando o arquivo de settings de core