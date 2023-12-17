#### _Проект был создан Олегом Сунгуровским <safasgasc.asfg@gmail.com>_

# Cоциальный веб-сайт

Приложение веб-сайт для публикаций картинок из сети. Функционал сайта позволяет регистрировать пользователей с помощью 
Facebook, Twitter и Google. Пользователи могу подписываться на понравившегося автора, ставить лайки/дизлайки, комментировать
картинки других пользователей и выкладывать свои собственные используя закладку на любое изображение в интернете. Они также смогут
видеть внутриплатформенную активность пользователей, на которых подписаны.

Используемые технологии:

* Python 3
* Java Script
* Django
* Django debug toolbar
* Django extensions(для запуска сервера на протоколе HTTPS - только для разработки)
* Easy thumbnails
* Social Auth
* Postgresql
* Redis
* Docker Compose

## Запуск приложения используя Docker Compose

1. Создать папку для проекта и перейти в неё:
    ```bash
    mkdir mysite
    ```
    ```bash
    cd mysite
    ```

2. Клонировать репозиторий с помощью git: 
   ```bash
     git clone https://github.com/OlegSungyrovsky/python-final-diplom
   ```
    
3. Настройки Django для отправки почты - [инструкция](https://vivazzi.pro/ru/it/send-email-in-django/). 
    - Для среды разработки можно использовать настройку ```EMAIL_BACKEND = 'django.core.mail.backend.console.EmailBackend'```

4. Создать файл **.env.dev** со следующими полями:
   - Для авторизации через Social Auth:
      * Facebook - [инструкция](https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html)
      * Twitter - [инструкция](https://python-social-auth.readthedocs.io/en/latest/backends/twitter.html)
      * Google - [инструкция](https://python-social-auth.readthedocs.io/en/latest/backends/google.html#google-oauth2)
```
Django settings
SECRET_KEY=<секретный ключ для приложения Django>
DEBUG=<True or False(True только для среды разработки)>
ALLOWED_HOSTS=[список, содержащий адреса всех доменов, которые могут запускать ваш проект Django(обязательно добавте в него mysite.com)]>

Database settings
PG_ENGINE=<databse engin(default: postgres)>
PG_NAME=<database name>
PG_PORT=<database port(default: 5432)>
PG_HOST=<database host(with docker: db)>
PG_USER=<database user>
PG_PASSWORD=database user's password>

Email settings
EMAIL_HOST=<из инструкции в 1 пункте>
EMAIL_HOST_USER=<из инструкции в 1 пункте>
EMAIL_HOST_PASSWORD=<из инструкции в 1 пункте>
EMAIL_PORT=<из инструкции в 1 пункте>
EMAIL_USE_TLS=<из инструкции в 1 пункте>
or
EMAIL_USE_SSL=<из инструкции в 1 пункте>

Social Auth
- Facebook
SOCIAL_AUTH_FACEBOOK_KEY=<из инструкции Facebook>
SOCIAL_AUTH_FACEBOOK_SECRET=<из инструкции Facebook>
- Twitter
SOCIAL_AUTH_TWITTER_KEY=<из инструкции Twitter>
SOCIAL_AUTH_TWITTER_SECRET=<из инструкции Twitter>
- Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=<из инструкции Google>
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=<из инструкции Google>

Redis
REDIS_HOST='<(использовать 'redis' для docker)>'
REDIS_PORT=<по умолчанию '6379'>
REDIS_DB=<по умолчанию '0'>

Docker Postgres
POSTGRES_DB=<имя базы данных для Docker>
POSTGRES_USER=<пользователь базы данных для Docker>
POSTGRES_PASSWORD=<пароль пользователя базы данных для Docker>
```
5. Используя команды ниже запустить приложение. Оно будет доступно по адресу: http://127.0.0.1:8000/
    ```bash
    docker-compose build
    ```
    ```bash
    docker-compose up -d
    ```
6. Создание супер пользователя для доступа к панели администратора:
    ```bash
    docker exec -it social-website_web_1 /bin/sh
    ```
    ```bash
    python manage.py createsuperuser
    ```
    - Админ панель доступна по адресу: http://127.0.0.1:8000/admin/

Для использования сервера по протоколу HTTPS заменить команду [тут](docker-compose.yaml) как показано ниже:
<image src="https://i.ibb.co/Vqvp9dD/2023-12-17-14-19-59.png">

Сервер будет доступен по адресу: https://mysite.com:8000/
__Только для среды разработки!__ 