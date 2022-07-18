# Cервис прохождения опросов

Сервис прохождения опросов позволяет пользователям зарегестрироваться и пройти опрос. За ответы на вопросы начисляется валюта, которую можно потратить на смену фона в профиле. Также есть рейтинг пользователей, где можно посмотреть на какое количество вопросов ответили различные пользователи.

# Стек технологий

- сервис написан на Python с использованием веб-фреймворка Django
- база данных - SQLite
- система управления версиями - git

# Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
```bash
    git clone https://github.com/Evgenia789/poll-test-task.git
```
```bash
    cd poll-test-task
```
Cоздать и активировать виртуальное окружение:
```bash
    python -m venv venv
```
```bash
    source venv/Scripts/activate
```
```bash
    python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```bash
    pip install -r requirements.txt
```
Выполнить миграции:
```bash
    python manage.py migrate
```
Создайте суперпользователя:
```bash
    python manage.py createsuperuser
```
Запустить проект:
```bash
    python manage.py runserver
```
____
Ваш проект запустился на http://127.0.0.1:8000/    

