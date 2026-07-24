from django.contrib import admin
from .models import Edificio, FotoEdificio


class FotoEdificioInline(admin.TabularInline):
    model = FotoEdificio
    extra = 1


@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cidade',
        'bairro',
        'ano_construcao',
        'area_construida',
        'tipo_uso',
        'status',
        'visivel',
    ]

    search_fields = [
        'nome',
        'localizacao_textual',
        'cidade',
        'bairro',
    ]

    list_filter = [
        'cidade',
        'bairro',
        'tipo_uso',
        'status',
        'visivel',
    ]

    prepopulated_fields = {
        'slug': ('nome',)
    }

    inlines = [
        FotoEdificioInline,
    ]


@admin.register(FotoEdificio)
class FotoEdificioAdmin(admin.ModelAdmin):
    list_display = [
        'edificio',
        'legenda',
        'ordem',
        'visivel',
    ]

    list_filter = [
        'visivel',
        'edificio',
    ]