# CRUD
`<>`는 변수를 의미하고 생성하고 싶은 이름을 넣는 공간입니다.

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


