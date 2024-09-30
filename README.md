# Задание
### Необходимо разработать менеджер паролей с методами GET и POST. Пароль хранится в бд, привязанный к имени сервиса, который указывается при создании пароля.
Требования:
1. Пароли должны храниться в зашифрованном виде
2. Для хранения паролей можно использовать любую базу данных, однако она должна запускаться как docker-контейнер
3. Проект должен запускаться через docker-compose
4. Разместить код на любом доступном git-репозитории.
5. Описать файл README.md , описать как запустить проект.
6. Соблюдать единый code-style на протяжении всего проекта
7. Покрыть код тестами API:

POST `/password/{service_name}` - создаем пароль/заменяем существующий пароль.

GET `/password/{service_name}` - получить пароль по имени сервиса.

GET `/password/?service_name={part_of_service_name}` - провести поиск по part_of_service_name и выдать пароли с подходящими service_name.

Пример работы:
1. Клиент делает запрос на создание пароля.

Запрос:
POST `/password/yundex`
HTTP/1.1
content-type: application/json

`{`
    `"password": "very_secret_pass"`
}`

Ответ:

HTTP/1.1 200 OK
content-type: application/json

`{
    "password": "very_secret_pass",
}`

2. Клиент запрашивает пароль по имени сервиса
Запрос:

GET `/password/yundex` HTTP/1.1

Ответ:

accept: application/json

HTTP/1.1 200 OK

content-type: application/json

`{ 
    "password": "very_secret_pass",
    "service_name": "yundex"
}`

4. Клиент запрашивает пароль по части имени сервиса
Запрос:

GET `/password/?service_name=yun` HTTP/1.1

Ответ:

accept: application/json

HTTP/1.1 200 OK

content-type: application/json
`[
{ 
    "password": "very_secret_pass",
    "service_name": "yundex"
}  
]`

Всё, что не указано в задании, опционально.

## Начало работы.
Инструкция написана для Mac OS. Если у вас другая ОС, ищите команды для своей ОС.

### 0. Создаёте новый проект, в нём создаёте виртуальное окружение командой `python -m venv venv`

### 1. Клонируйте репозиторий: `git clone git@github.com:Pavel-Sokolov-dotcom/password_manager.git`

### 2. Создайте файл .env заполните его своими данными. Образец заполнения:
`SECRET_KEY = 'ваш секретный ключ для Django'`
`DEBUG = True`

`FERNET_KEY=ваш_ключ_для_кодирования_пароля`
__________________________________________
Как сделать FERNET_KEY:
1) открываете другую IDE, например вы копируете репозиторий на VS Code, открываете PyCharm (или наоборот):
2) устанавливаете библиотеку cryptography командой `pip install cryptography`
3) копируете этот код в файл.py

`from cryptography.fernet import Fernet`

`key = Fernet.generate_key()`

`print(key.decode())`

>>выдаст ключ
4) копируете ключ, возвращаетесь в ту IDE, в которой у вас файл с переменными окружения (.env)
5) вставляете ключ в переменную FERNET_KEY без кавычек. Должно получиться что-то такое:

`FERNET_KEY=RbYU0zOD9RXSV-Irkss8q0bRu-JOv2xH6UAq6K8GF_4=`
__________________________________________

Далее в файле .env заполняете данные БД, я использовал PostgreSQL.

`DB_NAME=name_of_your_bd`

`DB_USER=your_user_for_bd`

`DB_PASSWORD=your_pass_for_bd`

`DB_HOST=db`

`DB_PORT=5432`



`POSTGRES_USER=user_for_your_PostgreSQL_bd`

`POSTGRES_PASSWORD=password`

`POSTGRES_DB=name_of_your_database`


### 3. Открываете терминал. Нужно проверить установлены ли Docker и Docker-compose.
 3.1 Проверить установлен ли Docker:
   `docker --version`
   Если Docker установлен, то в терминале увидете версию.
   
   Если Docker не установлен, то вам нужно его установить.
   
   Если не знаете как установить, то [вот](https://google-poisk-vmesto-tebya.ru/?q=%D0%BA%D0%B0%D0%BA%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C%20Docker)
   
 3.2 Проверить установлен ли Docker Compose:
   `docker-compose --version`
   Если Docker Compose не установлен, то вам нужно его установить.
   
   Если не знаете как установить, то [вот](https://google-poisk-vmesto-tebya.ru/?q=%D0%BA%D0%B0%D0%BA%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C%20Docker%20Compose)

### 4. Постройте и запустите контейнеры Docker Compose:
`docker-compose up --build`

### 5. При первом запуске проекта вам нужно создать и применить миграции для вашей БД, выполните эти команды для Docker Compose:
`docker-compose exec password_manager_get_post python manage.py makemigrations`

`docker-compose exec password_manager_get_post python manage.py migrate`

### 6. Откройте программу Postman. Выберете отправку POST-запроса
на адрес 
`http://localhost:8000/api/password/yundex/`

перейдите ниже в Body/raw выберите JSON, напишите следующее:


`{
    "password": "very_secret_pass"
}`

нажмите SEND. 

Вы должны получить ответ:

HTTP/1.1 200 OK
content-type: application/json
`{
     "password": "very_secret_pass",
     "service_name": "yundex"
}`

### 7. На данный момент задание выполнено на 80%

Изображения "Password_project_POST.png" и "Password_project_GET.png" показывают, как работают запросы POST и GET.

Пароли записываются и шифруются при запросах POST/GET для `http://localhost:8000/api/password/yundex/`

В ответ на `http://localhost:8000/api/password/?service_name=yun` программа выводит зашифрованный пароль.

В файле password_manager_get_post/accounts_passwords/tests.py не работают тесты.

Со временем доделаю эти два пункта.
