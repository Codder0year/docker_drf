from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='media/course_previews/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Уроки"
        verbose_name = "Урок"