# CRUD
`<>`는 변수를 의미하고 생성하고 싶은 이름을 넣는 공간입니다.

## 프로젝트 구조 생성

1. 프로젝트 폴더 생성
2. 프로젝트 폴더로 이동 / vscode 실행
    - `.gitignore`, `readme.md` 생성

3. django 프로젝트 생성
    - `<pjt-name>` 에는 생성하고 싶은 프로젝트의 이름을 작성합니다.
```bash
django-admin startproject <pjt-name>
```
4. 가상환경 설정
```bash
python -m venv venv
```

5. 가상환경 활성화
```bash
source venv/Scripts/activate
```

6. 가상환경에 django 설치
```bash
pip install django
```

7. 서버 실행 확인
```bash
python manage.py runserver
```

8. 앱 생성
```bash
django-admin startapp <app-name>
```

9. 앱 등록 => `settings.py`
```python
INSTALLED_APPS = [
    ....
    <app_name>
]
```

10. urls.py => views.py => templates/*.html 문서로 코드 작성


## Model

1. 모델 정의 (`models.py`)
    - 모델의 이름은 기본적으로 단수형태

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

2. 번역본 생성
```bash
python manage.py makemigrations
```

3. DB에 반영
```bash
python manage.py migrate
```

4. sql 스키마 확인
```bash
python manage.py sqlmigrate posts 0001
```

5. 생성한 모델을 admin에 등록(admin.py에)
```python
from .models import Post
# Register your models here.

admin.site.register(Post)
```

6. 관리자 계정 생성
```bash
python manage.py createsuperuser
```


## CRUD 로직 작성

### 1. Read

- 전체 게시물 출력
```python
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html',context)                  
```

### 2. Create

- 사용자에게 입력 할 수 있는 폼을 제공
```python
def new(request):
    return render(request, 'new.html')
```

- 사용자가 입력한 데이터를 가지고 DB에 저장하는 로직
```python
def create(request):
    
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')

```
### 3. Delete
```python
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')
```

### 4. Update
- 기존의 정보를 담은 form을 제공
```python
def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }

    return render(request, 'edit.html', context)
```

- 사용자가 입력한 새로운 정보를 가져와서
- 기존정보에 덮어씌우기

