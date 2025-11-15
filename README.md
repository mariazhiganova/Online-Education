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
- nginx

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

## Настройка удаленного сервера

#### Требования к серверу

    Ubuntu 20.04+

    Docker и Docker Compose

    Открытые порты: 80 (HTTP), 443 (HTTPS), 22 (SSH)

#### Установка на сервер

## Обновление и установка Docker

```
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Установка Docker Compose

```
sudo apt install docker-compose-plugin
```

## Добавление пользователя в группу docker

```
sudo usermod -aG docker $USER
```

## Настройка безопасности

```
SSH доступ только по ключам

Firewall: sudo ufw allow 22,80,443 && sudo ufw enable
```

## Автоматический деплой (CI/CD)

При каждом push в репозиторий автоматически:

#### Тестирование

    Запускаются все тесты Django

    Проверяется качество кода (flake8)

    Используется PostgreSQL + Redis

#### Деплой

    develop ветка → деплой на тестовый сервер

    main ветка → деплой на продакшен сервер

#### В Secrets в GitHub необходимо добавить:

    SECRET_KEY - секретный ключ Django

    SERVER_IP - IP вашего сервера

    SSH_PRIVATE_KEY - приватный SSH ключ

    DOCKERHUB_USERNAME и DOCKERHUB_TOKEN - для Docker Registry

## Доступ к приложению

Приложение доступно по IP: `158.160.202.72`

## Автор
**Мария Жиганова** - Backend Developer (Python)

```
GitHub - https://github.com/mariazhiganova
```
