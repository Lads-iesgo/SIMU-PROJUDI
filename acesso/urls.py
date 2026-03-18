from django.urls import path

from .views import  cadastrar, login_view
from .views_admin_usuarios import usuario_atualizar, usuario_lista

app_name = "acesso"

urlpatterns = [

    path("", login_view, name="login"),
    path("cadastro/", cadastrar, name="cadastro"),

    # Gestão de usuários
    path("usuarios/", usuario_lista, name="usuario_lista"),
    path("usuarios/atualizar/", usuario_atualizar, name="usuario_atualizar"),
]
