from django.shortcuts import render, redirect
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


def new(request):
    return render(request, 'new.html')

def create(request):
    # print(request)
    title = request.GET.get('title')
    content = request.GET.get('content')

    # print(title, content)

    post = Post()
    post.title = title
    post.content = content
    # print(post)
    post.save()

    return redirect(f'/posts/{post.id}/')


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')