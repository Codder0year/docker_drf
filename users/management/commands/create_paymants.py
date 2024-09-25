from django.core.management.base import BaseCommand
from users.models import User, Payments
from materials.models import Course, Lesson


class Command(BaseCommand):
    help = 'Создание платежей'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        if users.count() < 3:
            self.stdout.write(self.style.ERROR('Недостаточно пользователей'
                                               ' для создания платежей.'))
            return

        # Добавляем платежи
        Payments.objects.create(
            user=users[2],
            course=courses[0],
            amount=1500.00,
            payment_method='cash'
        )

        if lessons.count() > 0:
            Payments.objects.create(
                user=users[3],
                lesson=lessons[0],
                amount=800.00,
                payment_method='transfer'
            )

        self.stdout.write(self.style.SUCCESS('Платежи успешно созданы!'))
