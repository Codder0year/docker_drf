from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='media/avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('materials.Course', null=True, blank=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey('materials.Lesson', null=True, blank=True, on_delete=models.SET_NULL)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=
        [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
        ])


    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


    def __str__(self):
        return f'{self.user} - {self.amount}'
