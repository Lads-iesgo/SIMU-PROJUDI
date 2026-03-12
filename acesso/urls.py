from django.urls import path
from . import views

urlpatterns = [
    path('', views.acesso_view, name='acesso'),
]
    