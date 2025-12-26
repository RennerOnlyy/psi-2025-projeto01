# Generated migration to populate initial player data

from django.db import migrations
from datetime import date


def populate_jogadores(apps, schema_editor):
    Jogador = apps.get_model('posts', 'Jogador')
    
    jogadores_data = [
        {'nome': 'Hugo Souza', 'idade': 24, 'posicao': 'goleiro', 'nascimento': date(2001, 1, 1), 'foto': 'https://static.corinthians.com.br/uploads/1746024997d85b63ef0ccb114d0a3bb7b7d808028f.png'},
        {'nome': 'Matheuzinho', 'idade': 26, 'posicao': 'lateral_direito', 'nascimento': date(1999, 5, 12), 'foto': 'https://static.corinthians.com.br/uploads/1746025215c570c225d1fb8a72ad79995dd17a77bc.png'},
        {'nome': 'Félix Torres', 'idade': 28, 'posicao': 'zagueiro', 'nascimento': date(1997, 11, 14), 'foto': 'https://static.corinthians.com.br/uploads/1746024711841b60e20ff680b0d59aa9d6902fe289.png'},
        {'nome': 'André Ramalho', 'idade': 33, 'posicao': 'zagueiro', 'nascimento': date(1992, 4, 12), 'foto': 'https://static.corinthians.com.br/uploads/17460237847a98af17e63a0ac09ce2e96d03992fbc.png'},
        {'nome': 'Fabrizio Angileri', 'idade': 31, 'posicao': 'lateral_esquerdo', 'nascimento': date(1994, 7, 27), 'foto': 'https://static.corinthians.com.br/uploads/1746024168517da335fd0ec2f4a25ea139d5494163.png'},
        {'nome': 'Maycon', 'idade': 28, 'posicao': 'volante', 'nascimento': date(1997, 2, 15), 'foto': 'https://static.corinthians.com.br/uploads/1746025286c5ab6cebaca97f7171139e4d414ff5a6.png'},
        {'nome': 'Rodrigo Garro', 'idade': 25, 'posicao': 'meio_campista', 'nascimento': date(2000, 3, 7), 'foto': 'https://static.corinthians.com.br/uploads/1746024742a7a3d70c6d17a73140918996d03c014f.png'},
        {'nome': 'André Carrillo', 'idade': 33, 'posicao': 'extremo', 'nascimento': date(1990, 6, 29), 'foto': 'https://static.corinthians.com.br/uploads/174602440064de166633d61c8326232568b42beef1.png'},
        {'nome': 'Memphis Depay', 'idade': 31, 'posicao': 'atacante', 'nascimento': date(1994, 2, 13), 'foto': 'https://static.corinthians.com.br/uploads/1746025309a160a01c5ced2a79bc07e2b2ef1a2ada.png'},
        {'nome': 'Yuri Alberto', 'idade': 25, 'posicao': 'atacante', 'nascimento': date(1999, 3, 26), 'foto': 'https://static.corinthians.com.br/uploads/1746025501c2ed25e9f9b76909fc54491a253a5066.png'},
        {'nome': 'Talles Magno', 'idade': 23, 'posicao': 'atacante', 'nascimento': date(2002, 6, 26), 'foto': 'https://static.corinthians.com.br/uploads/1746025445be341249df108cb23c312ae62b6565cd.png'},
    ]
    
    for jog in jogadores_data:
        Jogador.objects.create(**jog)


def reverse_jogadores(apps, schema_editor):
    Jogador = apps.get_model('posts', 'Jogador')
    Jogador.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_informacao_jogador'),
    ]

    operations = [
        migrations.RunPython(populate_jogadores, reverse_jogadores),
    ]
