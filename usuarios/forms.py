from django import forms
from django.contrib.auth.models import User

from .models import PerfilUsuario


class CadastroUsuarioForm(forms.Form):
    nome_completo = forms.CharField(
        max_length=150,
        label='Nome completo'
    )

    email = forms.EmailField(
        label='E-mail'
    )

    empresa = forms.CharField(
        max_length=150,
        required=False,
        label='Empresa, se aplicável'
    )

    senha = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha'
    )

    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmar senha'
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if User.objects.filter(username=email).exists():
            raise forms.ValidationError('Já existe uma conta com este e-mail.')

        return email

    def clean(self):
        cleaned_data = super().clean()

        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não são iguais.')

        return cleaned_data

    def save(self):
        nome_completo = self.cleaned_data['nome_completo']
        email = self.cleaned_data['email']
        empresa = self.cleaned_data.get('empresa', '')
        senha = self.cleaned_data['senha']

        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome_completo
        )

        PerfilUsuario.objects.create(
            usuario=usuario,
            nome_completo=nome_completo,
            empresa=empresa,
            status_aprovacao='pendente',
        )

        return usuario