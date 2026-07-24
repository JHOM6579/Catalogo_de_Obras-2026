from django.contrib import admin
from .models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'usuario',
        'empresa',
        'telefone',
        'status_aprovacao',
        'criado_em',
    ]

    list_filter = [
        'status_aprovacao',
        'criado_em',
    ]

    search_fields = [
        'nome_completo',
        'usuario__username',
        'usuario__email',
        'empresa',
    ]

    readonly_fields = [
        'aprovado_por',
        'aprovado_em',
        'criado_em',
        'atualizado_em',
    ]

    actions = [
        'aprovar_usuarios',
        'bloquear_usuarios',
    ]

    def aprovar_usuarios(self, request, queryset):
        for perfil in queryset:
            perfil.aprovar(request.user)

    aprovar_usuarios.short_description = 'Aprovar usuários selecionados'

    def bloquear_usuarios(self, request, queryset):
        queryset.update(status_aprovacao='bloqueado')

    bloquear_usuarios.short_description = 'Bloquear usuários selecionados'