# Указываем базовый образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Не создавать виртуальное окружение
RUN poetry config virtualenvs.create false

# Копируем файлы pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root

# Копируем остальные файлы проекта в контейнер
COPY . .

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]