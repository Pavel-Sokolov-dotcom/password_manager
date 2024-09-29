# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /code

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /code/

# Указываем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]