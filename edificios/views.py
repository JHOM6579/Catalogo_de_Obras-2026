from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Edificio


def lista_edificios(request):
    busca = request.GET.get('busca', '').strip()

    edificios = Edificio.objects.filter(visivel=True)

    if busca:
        edificios = edificios.filter(nome__icontains=busca)

    context = {
        'edificios': edificios,
        'busca': busca,
    }

    return render(request, 'edificios/lista.html', context)


@login_required
def detalhe_edificio(request, slug):
    perfil = getattr(request.user, 'perfil', None)

    print('USUARIO:', request.user)
    print('IS_STAFF:', request.user.is_staff)
    print('PERFIL:', perfil)
    print('STATUS:', perfil.status_aprovacao if perfil else 'sem perfil')

    if not request.user.is_staff:
        if not perfil or not perfil.esta_aprovado:
            return redirect('aguardando_aprovacao')

    edificio = get_object_or_404(
        Edificio,
        slug=slug,
        visivel=True
    )

    fotos = edificio.fotos.filter(visivel=True)

    context = {
        'edificio': edificio,
        'fotos': fotos,
    }

    return render(request, 'edificios/detalhe.html', context)