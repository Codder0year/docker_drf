from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Создание тестовых пользователей'

    def handle(self, *args, **kwargs):
        for i in range(1, 5):  # Создание 4 тестовых пользователей
            email = f'test_user{i}@example.com'
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(email, 'testpassword')
        self.stdout.write(self.style.SUCCESS('Тестовые пользователи успешно созданы!'))