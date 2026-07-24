from django.db import models
from django.utils.text import slugify


class Edificio(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    descricao_curta = models.TextField(blank=True)
    descricao_completa = models.TextField(blank=True)

    localizacao_textual = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=50, blank=True)

    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)

    area_construida = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    area_terreno = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ano_construcao = models.PositiveIntegerField(null=True, blank=True)

    numero_pavimentos = models.PositiveIntegerField(null=True, blank=True)
    numero_unidades = models.PositiveIntegerField(null=True, blank=True)
    vagas_estacionamento = models.PositiveIntegerField(null=True, blank=True)

    tipo_uso = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)

    estrutura = models.CharField(max_length=150, blank=True)
    sistema_construtivo = models.CharField(max_length=150, blank=True)
    arquiteto = models.CharField(max_length=150, blank=True)
    cliente = models.CharField(max_length=150, blank=True)
    responsaveis_tecnicos = models.TextField(blank=True)

    diferenciais = models.TextField(blank=True)
    observacoes_internas = models.TextField(blank=True)

    visivel = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Edifício'
        verbose_name_plural = 'Edifícios'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nome)
            slug = base_slug
            contador = 1

            while Edificio.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                contador += 1
                slug = f'{base_slug}-{contador}'

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    @property
    def fotos_card(self):
        return self.fotos.filter(visivel=True).order_by('ordem', 'id')[:3]


class FotoEdificio(models.Model):
    edificio = models.ForeignKey(
        Edificio,
        related_name='fotos',
        on_delete=models.CASCADE
    )

    imagem = models.ImageField(upload_to='edificios/fotos/')
    legenda = models.CharField(max_length=200, blank=True)
    ordem = models.PositiveIntegerField(default=0)
    visivel = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', 'id']
        verbose_name = 'Foto do edifício'
        verbose_name_plural = 'Fotos dos edifícios'

    def __str__(self):
        return f'{self.edificio.nome} - Foto {self.id}'