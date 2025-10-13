from django.core.management import BaseCommand

from materials.models import Lesson
from users.models import CustomUser, Payment


class Command(BaseCommand):
    help = 'Fill payments with test data'

    def handle(self, *args, **options):
        user, created = CustomUser.objects.get_or_create(
            email='example@mail.com', defaults={'password': '123456'})

        lesson = Lesson.objects.first()

        if not lesson:
            self.stdout.write(self.style.ERROR('No lessons found in database!'))
            return

        payments = [
            {"user": user, "lesson": lesson, "sum": 1000, "payment_method": "cash"},
            {"user": user, "lesson": lesson, "sum": 2000, "payment_method": "card"},
            {"user": user, "lesson": lesson, "sum": 3000, "payment_method": "cash"},
        ]

        for payment_data in payments:
            payment, created = Payment.objects.get_or_create(**payment_data)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added payment: {payment.__str__()}'))
            else:
                self.stdout.write(self.style.WARNING(f'Payment already exists: {payment.__str__()}'))
