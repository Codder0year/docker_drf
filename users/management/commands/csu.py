from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from users.models import User


class Command(BaseCommand):
    help = 'Создание суперпользователя с фиксированным email и паролем'

    def handle(self, *args, **options):
        User = get_user_model()
        email = 'admin@example.com'
        password = 'adminpassword'

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING('Пользователь с таким email уже существует'))
            return

        User.objects.create_superuser(email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Суперпользователь {email} успешно создан'))