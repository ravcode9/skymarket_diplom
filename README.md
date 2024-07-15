# Skymarket - дипломный проект backend-части для сайта объявлений

## Автор

Равиль Латыпов (группа Python-разработчик 30.0)

## Описание проекта

Skymarket - это backend-часть для сайта объявлений. В проекте реализуется API для взаимодействия с базой данных объявлений, управления пользователями и обработки отзывов.

## Основной функционал

- Авторизация и аутентификация пользователей
- Распределение ролей (пользователь и админ)
- CRUD операции для объявлений
- Система отзывов под объявлениями
- Поиск объявлений по названию

## Технологии

- Python 3.12
- Django 5.0+
- Django Rest Framework
- PostgreSQL
- Djoser (для аутентификации)

## Установка и запуск

1. Клонируйте репозиторий: **git clone https://github.com/ravcode9/skymarket_diplom**
2. Перейдите в директорию проекта: **cd skymarket_diplom\skymarket**
3. Создайте и активируйте виртуальное окружение: **python -m venv venv**
**source venv/bin/activate**  (Для Linux/MacOS)
**venv\Scripts\activate**  (Для Windows)
4. Установите зависимости: **pip install -r requirements.txt**
5. Создайте файл `.env` в корневой директории проекта. Добавьте переменные окружения из .env.sample со своими значениями
6. Примените миграции: **python manage.py migrate**
7. Запустите сервер: **python manage.py runserver**

## Эндпоинты
### Объявления
- **GET /ads/** - Получить список объявлений
- **GET /ads/{id}/** - Получить детали объявления
- **PUT /ads/{id}/** - Обновить объявление
- **PATCH /ads/{id}/** - Частично обновить объявление
- **DELETE /ads/{id}/** - Удалить объявление

### Пользователи
- **GET /users/** - Получить список пользователей
- **POST /users/** - Создать нового пользователя
- **GET /users/{id}/** - Получить детали пользователя
- **PUT /users/{id}/** - Обновить пользователя
- **PATCH /users/{id}/** - Частично обновить пользователя
- **DELETE /users/{id}/** - Удалить пользователя

### Комментарии
- **GET /comments/** - Получить список комментариев
- **POST /comments/** - Создать новый комментарий
- **GET /comments/{id}/** - Получить детали комментария
- **PUT /comments/{id}/** - Обновить комментарий
- **PATCH /comments/{id}/** - Частично обновить комментарий
- **DELETE /comments/{id}/** - Удалить комментарий

## URL конфигурации

### Админ и задачи Redoc
- **admin/** - Административная панель
- **redoc-tasks/** - Задачи Redoc

### Пользователи
- **^users/$** - Список пользователей (name='users-list')
- **^users/activation/$** - Активация пользователей (name='users-activation')
- **^users/me/$** - Информация о текущем пользователе (name='users-me')
- **^users/resend_activation/$** - Повторная отправка активационного письма (name='users-resend-activation')
- **^users/reset_password/$** - Сброс пароля (name='users-reset-password')
- **^users/reset_password_confirm/$** - Подтверждение сброса пароля (name='users-reset-password-confirm')
- **^users/reset_email/$** - Сброс email (name='users-reset-username')
- **^users/reset_email_confirm/$** - Подтверждение сброса email (name='users-reset-username-confirm')
- **^users/set_password/$** - Установка нового пароля (name='users-set-password')
- **^users/set_email/$** - Установка нового email (name='users-set-username')
- **^users/(?P<id>[^/.]+)/$** - Детали пользователя (name='users-detail')

### Токен аутентификация
- **token/** - Получение JWT токена (name='token_obtain_pair')
- **refresh/** - Обновление JWT токена (name='token_refresh')

### Объявления
- **^ads/$** - Список объявлений (name='ad-list')
- **^ads\.(?P<format>[a-z0-9]+)/?$** - Список объявлений в формате (name='ad-list')
- **ads/me/$** - Получение объявлений текущего пользователя (name='ad-get-my-ads')
- **ads/me\.(?P<format>[a-z0-9]+)/?$** - Получение объявлений текущего пользователя в формате (name='ad-get-my-ads')
- **ads/(?P<pk>[^/.]+)/$** - Детали объявления (name='ad-detail')
- **ads/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$** - Детали объявления в формате (name='ad-detail')

### Комментарии к объявлениям
- **^ads/(?P<ad_pk>\d+)/comments/$** - Список комментариев к объявлению (name='ad-comments-list')
- **^ads/(?P<ad_pk>\d+)/comments\.(?P<format>[a-z0-9]+)/?$** - Список комментариев к объявлению в формате (name='ad-comments-list')
- **^ads/(?P<ad_pk>\d+)/comments/(?P<pk>[^/.]+)/$** - Детали комментария к объявлению (name='ad-comments-detail')
- **^ads/(?P<ad_pk>\d+)/comments/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$** - Детали комментария к объявлению в формате (name='ad-comments-detail')

### Прочее
- **[name='api-root']** - Корневой эндпоинт API
- **<drf_format_suffix:format>** - Суффиксы формата для API (name='api-root')

#### Swagger и Redoc
- **swagger/** - Swagger UI  документация (name='schema-swagger-ui')
- **redoc/** - Redoc документация (name='schema-redoc')

### Медиафайлы
- **^django_media/(?P<path>.*)$** - URL для доступа к медиафайлам

## Роли пользователей

- **Админ**: Полный доступ ко всем объявлениям и комментариям
- **Пользователь**: Может создавать, редактировать и удалять только свои объявления и комментарии
- Неавторизованный пользователь может только просматривать объявления и комментарии

## Поиск (Фильтрация)

Поиск объявлений возможно осуществить по названию через параметр `?title=` в GET-запросе `/ads/?title=<часть названия>`.

## Примеры http запросов RESTful API

- Для авторизации используйте JWT токен через POST localhost:8000/token/, скопируйте и вставьте токен в поле Authorization в Headers в таком виде: "Bearer <ваш токен>"
- Запросы можно отправлять через программу Postman

### Регистрация нового пользователя

**POST** localhost:8000/api/users/
**Content-Type**: application/json
{
**"email"**: "user@example.com",
**"first_name"**: "string",
**"last_name"**: "string",
**"password"**: "string",
**"phone"**: "string",
**"image"**: "http://example.com"
}

### Создание нового объявления

**POST** localhost:8000/ads/
**Content-Type**: application/json
{
**"image"**: "http://example.com",
**"title"**: "string",
**"price"**: 2147483647,
**"description"**: "string"
}
