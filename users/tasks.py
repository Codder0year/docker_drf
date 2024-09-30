from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


@shared_task
def deactivate_inactive_users():
    one_month_ago = timezone.now() - timedelta(days=30)

    # Получаем пользователей, которые не входили в систему более месяца
    inactive_users = User.objects.filter(last_login__lt=one_month_ago,
                                         is_active=True)

    # Блокируем пользователей
    inactive_users.update(is_active=False)
    return f"Деактивация {inactive_users.count()} неактивных пользователей."