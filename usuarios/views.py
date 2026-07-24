from django.shortcuts import redirect, render

from .forms import CadastroUsuarioForm


def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('aguardando_aprovacao')
    else:
        form = CadastroUsuarioForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})


def aguardando_aprovacao(request):
    return render(request, 'usuarios/aguardando_aprovacao.html')