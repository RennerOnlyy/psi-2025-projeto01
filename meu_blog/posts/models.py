from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Conteúdo")
    publication_date = models.DateTimeField(default=timezone.now, verbose_name="Data de Publicação")
    image = models.ImageField(upload_to='post_images/', verbose_name="Imagem")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"


class Jogador(models.Model):
    POSICOES = [
        ('goleiro', 'Goleiro'),
        ('lateral_direito', 'Lateral Direito'),
        ('lateral_esquerdo', 'Lateral Esquerdo'),
        ('zagueiro', 'Zagueiro'),
        ('volante', 'Volante'),
        ('meio_campista', 'Meio-campista'),
        ('extremo', 'Extremo/Direita'),
        ('atacante', 'Atacante'),
    ]

    nome = models.CharField(max_length=150, verbose_name="Nome")
    idade = models.IntegerField(verbose_name="Idade")
    posicao = models.CharField(max_length=20, choices=POSICOES, verbose_name="Posição")
    nascimento = models.DateField(verbose_name="Data de Nascimento")
    foto = models.URLField(verbose_name="URL da Foto")

    def __str__(self):
        return f"{self.nome} - {self.get_posicao_display()}"

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"
        ordering = ['nome']


class Informacao(models.Model):
    chave = models.CharField(max_length=100, unique=True, verbose_name="Chave")
    valor = models.TextField(verbose_name="Valor")

    def __str__(self):
        return self.chave

    class Meta:
        verbose_name = "Informação"
        verbose_name_plural = "Informações"