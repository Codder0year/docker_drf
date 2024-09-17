from rest_framework import serializers
from .models import Payments, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
