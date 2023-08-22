from django.shortcuts import render
# Post 모델을 import
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'index.html', context)


# post = Post.objects.get(id=id)의 첫번째 아이디는 
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }

    return render(request, 'detail.html', context)