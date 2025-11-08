# Online Education - Образовательный онлайн-сервис

Система для учителей и учеников с уроками собранными в курсы

## Возможности

- Создание уроков и курсов
- Подписки на курсы
- Автоматические письма на почту при изменении курса

## Технологии

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL
- **Task Queue**: Celery + Redis
- **Notifications**: Email
- **Auth**: JWT-аутентификация
- **Containerization**: Docker + Docker Compose

# Установка и запуск

### Клонирование репозитория

```bash
git clone https://github.com/mariazhiganova/Online-Education.git
```

### Настройка окружения

Создайте файл .env на основе .env.example

### Установка зависимостей

```
poetry install
poetry shell
```

## Установка через Docker (рекомендуется)

### 1. Выполните команду

```
docker-compose up -d
```

### 2. Проверьте статус и работоспособность

```
docker-compose ps
```

#### Должны быть в статусе Up:

- web - основное приложение
- db - база данных
- redis - кэш и очереди задач
- celery - фоновые задачи

#### Проверить логи можно следующей командой:

```
docker-compose logs
```

#### Перейти по ссылке (должна открываться страница списка уроков)

http://localhost:8000/lessons/list/

### 3. Остановка

```
docker-compose down
```

## Ручной запуск (без Docker)

### 1. Установите зависимости

```
poetry install
poetry shell
```

### 2. Запустите сервер

```
python manage.py migrate
python manage.py runserver
```

### 3. Celery (в отдельном терминале)

```
-A config worker -l INFO
```

## Документация

Вы можете увидеть документацию API, перейдя по URL-адресу

Для Swagger:

```
http://localhost:8000/swagger/
```

Для Redoc:

```
http://localhost:8000/redoc/
```

## Автор

**Мария Жиганова** - Backend Developer (Python)

```
GitHub - https://github.com/mariazhiganova
```
