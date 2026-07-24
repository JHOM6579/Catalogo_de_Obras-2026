from django.conf import settings
from django.db import models
from django.utils import timezone


class PerfilUsuario(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('bloqueado', 'Bloqueado'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    nome_completo = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    justificativa_acesso = models.TextField(blank=True)

    status_aprovacao = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    aprovado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='usuarios_aprovados'
    )

    aprovado_em = models.DateTimeField(null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil de usuário'
        verbose_name_plural = 'Perfis de usuários'

    def __str__(self):
        return self.nome_completo

    @property
    def esta_aprovado(self):
        return self.status_aprovacao == 'aprovado'

    def aprovar(self, admin_user):
        self.status_aprovacao = 'aprovado'
        self.aprovado_por = admin_user
        self.aprovado_em = timezone.now()
        self.save()