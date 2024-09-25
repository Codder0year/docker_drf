from django.urls import path
from rest_framework.permissions import AllowAny

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'Course', CourseViewSet, basename='Course')
urlpatterns = [
    path('Lesson/create', LessonCreateAPIView.as_view(), name='Lesson-create'),
    path('Lesson/', LessonListAPIView.as_view(), name='Lesson-list'),
    path('Lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='Lesson-detail'),
    path('Lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(permission_classes = [AllowAny]), name='Lesson-update'),
    path('Lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(permission_classes = [AllowAny]), name='Lesson-delete'),
    path('subscribe/', SubscriptionAPIView.as_view(), name='subscribe')
    ] + router.urls
