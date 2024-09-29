# Задание
# Необходимо разработать менеджер паролей с методами GET и POST. Пароль хранится в бд, привязанный к имени сервиса, который указывается при создании пароля.

Требования:
1. Пароли должны храниться в зашифрованном виде
2. Для хранения паролей можно использовать любую базу данных, однако она должна запускаться как docker-контейнер
3. Проект должен запускаться через docker-compose
4. Разместить код на любом доступном git-репозитории.
5. Описать файл README.md , описать как запустить проект.
6. Соблюдать единый code-style на протяжении всего проекта
7. Покрыть код тестами API
Пример работы
1. Клиент делает запрос на создание пароля Запрос:
Ответ:
 POST /password/{service_name} - создаем пароль/заменяем существующий пароль GET /password/{service_name} - получить пароль по имени сервиса
- провести поиск по part_of_service_name и выдать пароли с подходящими service_name
GET /password/?service_name={part_of_service_name}
POST /password/yundex HTTP/1.1
content-type: application/json
{
    "password": "very_secret_pass"
}

HTTP/1.1 200 OK
content-type: application/json
{
    "password": "very_secret_pass",
}
2. Клиент запрашивает пароль по имени сервиса
Запрос:
Ответ:
GET /password/yundex HTTP/1.1
accept: application/json
HTTP/1.1 200 OK
content-type: application/json
{ 
    "password": "very_secret_pass",
    "service_name": "yundex"
}

3. Клиент запрашивает пароль по части имени сервиса
Запрос:
Ответ:
GET /password/?service_name=yun HTTP/1.1
accept: application/json
HTTP/1.1 200 OK
content-type: application/json
[

{ 
    "password": "very_secret_pass",
    "service_name": "yundex"
}

]

Всё, что не указано в задании, опционально.

## Начало работы.
1. Копируете себе репозиторий
