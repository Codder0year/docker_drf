from django.core.management.base import BaseCommand
from users.models import User
from materials.models import Course, Lesson


class Command(BaseCommand):
    help = 'Создание курсов и уроков'

    def handle(self, *args, **kwargs):
        # Создание тестового пользователя
        user, created = User.objects.get_or_create(
            email='test_user@example.com',
            defaults={'password': 'testpassword'}
        )

        # Создание курсов
        course1 = Course.objects.create(name='Курс 1', owner=user)
        course2 = Course.objects.create(name='Курс 2', owner=user)

        # Создание уроков
        Lesson.objects.create(name='Урок 1.1', course=course1, owner=user)
        Lesson.objects.create(name='Урок 1.2', course=course1, owner=user)
        Lesson.objects.create(name='Урок 2.1', course=course2, owner=user)

        self.stdout.write(self.style.SUCCESS('Курсы и уроки успешно созданы!'))
