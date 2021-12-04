# api_yamdb
Проект YaMDb собирает отзывы пользователей на различные произведения.
***
### Возможности:
* Регистрация и аутентификация пользователей
* Получение списка всех произведений
* Получение списка всех жанров
* Получение списка всех категорий
* Получение списка всех отзывов
* Получение списка всех комментариев к отзыву
* Получение списка всех пользователей
***
### Проект:
```
git clone git@github.com:WeiGOooo/infra_sp2.git
```
## Установка
1. Установка docker и docker-compose
```
https://docs.docker.com/engine/install/ubuntu/
```

2. Создать файл .env с переменными окружения
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # Имя базы данных
POSTGRES_USER=postgres # Администратор базы данных
POSTGRES_PASSWORD=postgres # Пароль администратора
DB_HOST=db
DB_PORT=5432
```
3. Сборка и запуск контейнера
```
docker-compose up -d --build
```
4. Миграции
```
docker-compose exec web python manage.py migrate
```
5. Создание суперпользователя Django
```
docker-compose exec web python manage.py createsuperuser
```
6. Сбор статики
```
docker-compose exec web python manage.py collectstatic --no-input
```

Документация доступна по адресу:
http://127.0.0.1/redoc/
***
### Пример работы API:

Запрос для создания поста:
```python
import requests
from pprint import pprint
url = 'http://127.0.0.1/api/v1/categories/'
request = requests.get(url).json()
pprint(request)
```
Ответ от API:
```json
{"count": 3,
 "next": "None",
 "previous": "None",
 "results": [{"name": "Фильм", "slug": "movie"},
             {"name": "Книга", "slug": "book"},
             {"name": "Музыка", "slug": "music"}]}
```
***
## Автор проекта:
* https://t.me/nazasyp
***
