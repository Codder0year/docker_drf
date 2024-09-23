from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Course, Lesson, Subscription
from users.models import User
from django.contrib.auth.models import Group


class CourseLessonTestCase(APITestCase):
    def setUp(self):
        # Создаем пользователя и группу
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.moderator_group = Group.objects.create(name='moderators')
        self.user.groups.add(self.moderator_group)

        # Создаем курс и урок
        self.course = Course.objects.create(name='Test Course', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test Lesson', course=self.course, link='https://youtube.com/test')

        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Проверка создания нового урока."""
        response = self.client.post(reverse('materials:Lesson-create'), {
            'name': 'New Lesson',
            'course': self.course.id,
            'link': 'https://youtube.com/new-lesson'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_lesson(self):
        """Проверка обновления существующего урока."""
        response = self.client.put(reverse('materials:Lesson-update', args=[self.lesson.id]), {
            'name': 'Updated Lesson',
            'course': self.course.id,
            'link': 'https://youtube.com/updated-lesson'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        """Проверка удаления урока."""
        response = self.client.delete(reverse('materials:Lesson-delete', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_subscribe_to_course(self):
        """Проверка подписки на курс."""
        response = self.client.post(reverse('materials:subscribe'), {
            'course': self.course.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_subscribe_already_exists(self):
        """Проверка поведения при повторной подписке на курс."""
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.post(reverse('materials:subscribe'), {
            'course': self.course.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка удалена')

    def test_unsubscribe_from_course(self):
        """Проверка отписки от курса."""
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.delete(reverse('materials:subscribe'), {
            'course': self.course.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_not_exists(self):
        """Проверка поведения при отписке от несуществующей подписки."""
        response = self.client.delete(reverse('materials:subscribe'), {
            'course': self.course.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка не найдена')

    def test_create_lesson_unauthenticated(self):
        """Проверка доступа к созданию урока для неаутентифицированного пользователя."""
        self.client.logout()
        response = self.client.post(reverse('materials:Lesson-create'), {
            'name': 'New Lesson',
            'course': self.course.id,
            'link': 'https://youtube.com/new-lesson'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def tearDown(self):
        # Очищаем тестовые данные
        self.lesson.delete()
        self.course.delete()
        self.user.delete()
        self.moderator_group.delete()

