#  Camada view:
#  Prover o roteamento de rotas,
#  Processar Requisições HTTP,
#  Aplicar as regras de negócio definidas para cada view
#  Formular Respostas HTTP, Recepcionar requisições http, Processa - lás e responde -  las


# Objeto HttpRequest

# Atributos:

# scheme  ->  Ex: http/https
# path    ->  Ex: "/funcionarios/cadastrar"
# method  ->  Ex: GET/POST
# headers ->  Contém o cabeçalho HTTP
# FILES  ->   Contém arquivos, caso algum tenha sido enviado.



from django.http import HttpRequest
from django.shortcuts import render

def home(requisicao: HttpRequest):  # pycharm não entende o que é a requisição, seu tipo primitivo. Por isso usamos type hint
    if requisicao.method == 'GET':  # Vamos verificar qual método http, dependendo do método, teremos um tipo de processamento
        return render(requisicao, template_name='erp/index.html')












