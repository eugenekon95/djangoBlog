from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/index.html',
                  {'posts': posts})

def show(request, id):
    post = get_object_or_404(Post,
                             id=id, status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/show.html',
                  {'post': post})