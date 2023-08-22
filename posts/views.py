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


# post = Post.objects.get(id=id)의 첫번째 아이디는 Post의 id임
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


def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }

    return render(request, 'edit.html', context)

def update(request, id):
    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    #post = Post() => 새로운 게시물을 만들 때
    # 기존 데이터 / 여기가 create와 다른 부분
    post = Post.objects.get(id=id)

    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')