from django.shortcuts import render


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
    """Exibe o elenco com 11 jogadores fornecidos via contexto (sem banco de dados)."""
    # 11 titulares reais (nomes atuais) — nascimento/idade podem ser ajustados conforme necessário
    jogadores = [
        {'nome': 'Hugo Souza', 'idade': 24, 'posicao': 'Goleiro', 'nascimento': '2001-01-01', 'foto': 'https://static.corinthians.com.br/uploads/1746024997d85b63ef0ccb114d0a3bb7b7d808028f.png'},
        {'nome': 'Matheuzinho', 'idade': 26, 'posicao': 'Lateral Direito', 'nascimento': '1999-05-12', 'foto': 'https://static.corinthians.com.br/uploads/1746025215c570c225d1fb8a72ad79995dd17a77bc.png'},
        {'nome': 'Félix Torres', 'idade': 28, 'posicao': 'Zagueiro', 'nascimento': '1997-11-14', 'foto': 'https://static.corinthians.com.br/uploads/1746024711841b60e20ff680b0d59aa9d6902fe289.png'},
        {'nome': 'André Ramalho', 'idade': 33, 'posicao': 'Zagueiro', 'nascimento': '1992-04-12', 'foto': 'https://static.corinthians.com.br/uploads/17460237847a98af17e63a0ac09ce2e96d03992fbc.png'},
        {'nome': 'Fabrizio Angileri', 'idade': 31, 'posicao': 'Lateral Esquerdo', 'nascimento': '1994-07-27', 'foto': 'https://static.corinthians.com.br/uploads/1746024168517da335fd0ec2f4a25ea139d5494163.png'},
        {'nome': 'Maycon', 'idade': 28, 'posicao': 'Volante', 'nascimento': '1997-02-15', 'foto': 'https://static.corinthians.com.br/uploads/1746025286c5ab6cebaca97f7171139e4d414ff5a6.png'},
        {'nome': 'Rodrigo Garro', 'idade': 25, 'posicao': 'Meio-campista', 'nascimento': '2000-03-07', 'foto': 'https://static.corinthians.com.br/uploads/1746024742a7a3d70c6d17a73140918996d03c014f.png'},
        {'nome': 'André Carrillo', 'idade': 33, 'posicao': 'Extremo/Direita', 'nascimento': '1990-06-29', 'foto': 'https://static.corinthians.com.br/uploads/174602440064de166633d61c8326232568b42beef1.png'},
        {'nome': 'Memphis Depay', 'idade': 31, 'posicao': 'Atacante/Extremo', 'nascimento': '1994-02-13', 'foto': 'https://static.corinthians.com.br/uploads/1746025309a160a01c5ced2a79bc07e2b2ef1a2ada.png'},
        {'nome': 'Yuri Alberto', 'idade': 25, 'posicao': 'Atacante', 'nascimento': '1999-03-26', 'foto': 'https://static.corinthians.com.br/uploads/1746025501c2ed25e9f9b76909fc54491a253a5066.png'},
        {'nome': 'Talles Magno', 'idade': 23, 'posicao': 'Atacante/Extremo', 'nascimento': '2002-06-26', 'foto': 'https://static.corinthians.com.br/uploads/1746025445be341249df108cb23c312ae62b6565cd.png'},
    ]
    context = {
        'jogadores': jogadores,
        'titulo': 'Elenco - Corinthians'
    }
    return render(request, 'posts/equipe.html', context)
def sobre(request):
    """Página Sobre, com informações do projeto e autores."""
    info = {
        'autores': ['Equipe Corinthians', 'Elias Renner'],
        'ano': 2025,
        'tecnologia': ['Django', 'Bootstrap 5'],
        'descricao': 'Site demonstrativo sem uso de banco de dados; todos os dados são fornecidos via contexto nas views.'
    }
    context = {
        'info': info,
        'titulo': 'Sobre - Corinthians'
    }
    return render(request, 'posts/sobre.html', context)
