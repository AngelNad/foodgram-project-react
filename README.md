## Проект "Продуктовый помощник"
Приложение развёрнуто по адресу:
**http://51.250.31.38**

### Описание
Проект — сайт Foodgram, «Продуктовый помощник». Онлайн-сервис и API для него. На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
К проекту по адресу http://51.250.31.38/api/docs/redoc.html подключена документация API Foodgram. В ней описаны возможные запросы к API и структура ожидаемых ответов. Для каждого запроса указаны уровни прав доступа: пользовательские роли, которым разрешён запрос.

### Технологии
- Python 3.7
- Django 2.2.16
- Djangorestframework 3.12.4


### Заполнение файла .env

_Создайте в директории /infra файл .env с переменными окружения для работы с базой данных со значениями:_
DB_ENGINE=django.db.backends.postgresql<br>
DB_NAME=postgres <br>
POSTGRES_USER=postgres <br>
POSTGRES_PASSWORD=postgres <br>
DB_HOST=db <br>
DB_PORT=5432

### Приложение работает на Docker-compose
Образ проекта на DockerHub **angelnad/foodgram-project** <br>
Образ для фронтенда на DockerHub **angelnad/foodgram-project** <br>

_**Workflow status badge:**_<br>
![Django-app-foodgram-project workflow](https://github.com/AngelNad/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

_Команды для запуска приложения в контейнерах:_
- Разверните контейнеры в папке /infra запустив docker-compose командой

```
docker-compose up
```
У вас развернётся проект с базой данных Postgres. <br>
Чтобы проверить его работу, перейдите по ссылке http://127.0.0.1:8000/admin/
- В папке /infra с файлом docker-compose.yaml создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```

### Заполнение базы:

```
docker-compose exec backend python manage.py loaddata > fixtures.json
```

### Создайте дамп (резервную копию) базы:

```
docker-compose exec backend python manage.py dumpdata > fixtures.json
```

### Автор:
Надежда Осипова

