# posts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

# View para a página inicial (lista de posts)
def index(request):
    # Busca todos os posts, ordenados pela data de publicação (mais recente primeiro)
    all_posts = Post.objects.all().order_by('-publication_date')
    context = {
        'all_posts': all_posts
    }
    return render(request, 'posts/index.html', context)

# View para a página de um post específico
def post_detail(request, post_id):
    # Busca o post pelo ID ou retorna um erro 404 se não encontrar
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)