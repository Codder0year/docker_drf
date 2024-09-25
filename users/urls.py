from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentsViewSet, UserCreateAPIView
from rest_framework_simplejwt.views import (TokenRefreshView,
                                            TokenObtainPairView)

router = DefaultRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
