from celery import shared_task
from django.core.mail import send_mail

from materials.models import Course, Subscription


@shared_task
def send_subscription_mail(course_id):
    """Отправка писем подписчикам курса при внесении изменений в курс"""
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)

    for sub in subscriptions:
        user = sub.user
        subject = f'Курс "{course.title}" обновлён!'
        message = f'В курсе "{course.title}" появились новые материалы. Заходите изучать!'
        from_email = 'my.nik.mariann@gmail.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
