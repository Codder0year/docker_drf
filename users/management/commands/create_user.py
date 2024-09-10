from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Создание тестовых пользователей'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='test_admin').exists():
            self.stdout.write(self.style.SUCCESS('Тестовые пользователи уже существуют.'))
            return

        # Создание тестовых пользователей
        User.objects.create_user('test_3', 'test_user1@example.com', 'testpassword')
        self.stdout.write(self.style.SUCCESS('Тестовые пользователи успешно созданы!'))