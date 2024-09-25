from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer
from users.services import (convert_rub_to_usd,
                            create_stripe_price,
                            create_stripe_session)


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method', 'link')
    ordering_fields = ('payment_date',)

    def perform_create(self, serializer):
        # Получаем сумму и конвертируем её в доллары
        amount_in_rub = serializer.validated_data['amount']
        amount_in_usd = convert_rub_to_usd(amount_in_rub)

        # Создаём продукт и цену в Stripe
        price = create_stripe_price(amount_in_usd)

        # Создаём сессию оплаты в Stripe
        session_id, payment_url = create_stripe_session(price.get('id'))

        # Сохраняем данные в модель Payments
        serializer.save(
            session_id=session_id,
            link=payment_url
        )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
