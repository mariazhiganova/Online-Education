from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import CustomUser


@shared_task
def block_inactive_users():
    """Блокировка пользователей, последний логин которых был более месяца назад"""
    month_ago = timezone.now() - relativedelta(months=1)

    inactive_users = CustomUser.objects.filter(last_login__lt=month_ago, is_active=True)

    for user in inactive_users:
        user.is_active = False
        user.save()
