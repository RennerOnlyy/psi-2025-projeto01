from django.contrib import admin
from .models import Post, Jogador, Informacao


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('title', 'content')
    ordering = ('-publication_date',)


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'posicao', 'idade')
    list_filter = ('posicao', 'idade')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Informacao)
class InformacaoAdmin(admin.ModelAdmin):
    list_display = ('chave', 'valor')
    search_fields = ('chave',)