from django.urls import path

from .views import home, redirecionamento_teste_sucesso


app_name = "base"

urlpatterns = [
    path("home/", home, name="home"),
    path("redirecionamento-teste-sucesso/", redirecionamento_teste_sucesso, name="redirecionamento_teste_sucesso"),
    
]
