# Quiz Api
API для системы опросов пользователей

## Функционал для администратора системы
- авторизация в системе
- добавление/изменение/удаление опросов
- добавление/изменение/удаление вопросов в опросе
- После создания поле "дата старта" у опроса менять нельзя (добавление/изменение/удаление вопросов в опросе)


## Функционал для пользователей системы
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно(в качестве идентификатора пользователя в API передаётся числовой ID)
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

## Установка 
  1. Cклонируйте репозитори
  2. Создайте вертуальное окружение
  3. Скачать зависимости ```pip install -r requirements.txt```
  4. Сделать миграцию
    4.1 ```python manage.py makemigrations```
    4.2 ```python manage.py migrate```
  5. Cоздать суперпользователя
    - ```python manage.py createsuperuser
  6. Запустить сервер локально
    - ```python manage.py runserver```

## Документация api
Авторизация:
  url ```api/jwt/token  ```
  method: ```post```
  parametrs: ```username, password```
  Получаем токен, передавайте токен в заголовке Authorization: JWT <token>
  
## Добавление опросов
  metohd: POST
  url: ```api/quiz/```
  parametrs: ```name end_date description```
  permission: ADMIN

### изменение/удаление опросов
  metohd: PUT, DELETE
  url: ```api/quiz/<quiz_id>/```
  permission: ADMIN
 
 ## Добавление вопросов
  metohd: POST
  url: ```api/quiz/<quiz_id>/questions```
  parametrs: ```question_text type quiz```
  permission: ADMIN
### изменение/удаление опросов
  metohd: PUT, DELETE
  url: ```api/quiz/<quiz_id>/questions/<question_id>/```
  permission: ADMIN
  
## Добавление вариантов ответа к вопросу
  metohd: POST
  url: ```api/quiz/<quiz_id>/questions/<question_id>/choices```
  parametrs: ```options```
  permission: ADMIN
  
## Получение списка активных опросов 
  metohd: GET
  url: ```api/active_quiz```
  
## Прохождение опроса
  metohd: POST
  url: ```api/quiz/<quiz_id>/questions/<question_id>/answers```
  parametrs: ```user_id```

## Список пройденных опросов пользователя
  metohd: GET
  url: ```api/user_quiz/<user_id>/```
