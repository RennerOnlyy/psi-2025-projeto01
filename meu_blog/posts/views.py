from django.shortcuts import render
from .models import Jogador, Informacao


def index(request):
    """Página inicial com tema do Sport Club Corinthians Paulista."""
    titulo = "Sport Club Corinthians Paulista"
    historico = (
        "O Sport Club Corinthians Paulista, conhecido como Corinthians ou Timão, "
        "é um dos maiores clubes do Brasil. Esta versão demonstra um site estático "
        "com informações do time principal sem utilização de banco de dados."
    )
    imagens = [
        "https://via.placeholder.com/900x300/000000/FFFFFF?text=Corinthians",
        "https://via.placeholder.com/400x250/000000/FFFFFF?text=Neo+Qu%C3%ADmica+Arena",
        "https://via.placeholder.com/400x250/000000/FFFFFF?text=Fiel"
    ]
    context = {
        'titulo': titulo,
        'historico': historico,
        'imagens': imagens,
    }
    return render(request, 'posts/inicio.html', context)


def equipe(request):
    """Exibe o elenco com os jogadores do banco de dados."""
    jogadores = Jogador.objects.all().order_by('nome')
    context = {
        'jogadores': jogadores,
        'titulo': 'Elenco - Corinthians'
    }
    return render(request, 'posts/equipe.html', context)


def sobre(request):
    """Página Sobre, com informações do projeto e autores."""
    info_dict = {}
    for info in Informacao.objects.all():
        info_dict[info.chave] = info.valor

    context = {
        'info': info_dict,
        'titulo': 'Sobre - Corinthians'
    }
    return render(request, 'posts/sobre.html', context)
