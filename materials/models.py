from django.db import models

from users.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='media/course_previews/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses', help_text='Владелец курса')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Курсы"
        verbose_name = "Курс"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='media/lesson_previews/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор", help_text="Автор урока")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Уроки"
        verbose_name = "Урок"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions')

    class Meta:
        unique_together = ('user', 'course')
        verbose_name_plural = "Подписки"
        verbose_name = "Подписка"

    def __str__(self):
        return f"{self.user.email} -> {self.course.name}"