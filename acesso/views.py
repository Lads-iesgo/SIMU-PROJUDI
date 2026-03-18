from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import CadastroPublicoForm, LoginForm




def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user()) 
      
        # todo: redirecionar para pagina de acordo com perfil
        if request.user.tipo_perfil_global == "Admin":
            return redirect("admin:index")
        
        if request.user.tipo_perfil_global == "Coordenador":
            return redirect("acesso:painel_administrativo")
        
        if request.user.tipo_perfil_global == "Professor":
            return redirect("acesso:usuario_lista")
        
        if request.user.tipo_perfil_global == "Aluno":
            return redirect("base:cadastro_processo")
        
        return redirect("base:redirecionamento_teste_sucesso")
    
    
    return render(request, "acesso/login.html", {"form": form})





def cadastrar(request):
    if request.method == "POST":
        form = CadastroPublicoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("base:redirecionamento_teste_sucesso")
    else:
        form = CadastroPublicoForm()

    return render(request, "acesso/cadastro_usuario.html", {"form": form})