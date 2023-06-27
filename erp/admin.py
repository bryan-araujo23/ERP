from django.contrib import admin
from .models import Funcionario, Produto, Venda

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Venda)
