from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscription, Course


@shared_task
def send_course_update_email(course_id):
    course = Course.objects.get(id=course_id)
    subscribers = Subscription.objects.filter(course=course)

    for subscription in subscribers:
        send_mail(
            subject=f"Обновление курса: {course.name}",
            message=f"Курс '{course.name}' был обновлен. Проверьте новые материалы",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscription.user.email],
        )