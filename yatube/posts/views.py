from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    title = 'Записи сообщества' + ' ' + group.title
    context = {
        'slug': slug,
        'text': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
