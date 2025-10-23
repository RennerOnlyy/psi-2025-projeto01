from django.db import models

# posts/models.py
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