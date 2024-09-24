import stripe
from django.conf import settings
from forex_python.converter import CurrencyRates


# Инициализация ключа Stripe
stripe.api_key = settings.STRIPE_API_KEY

# Функция конвертации RUB в USD
def convert_rub_to_usd(amount):
    """Конвертирует рубли в доллары."""
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(amount * rate)

# Создание продукта в Stripe
def create_product():
    """Создает продукт в Stripe."""
    return stripe.Product.create(name="Payments")

# Создание цены для продукта
def create_stripe_price(amount):
    """Создает цену в Stripe."""
    return stripe.Price.create(
        currency="usd",
        unit_amount=int(amount * 100),  # Сумма в центах
        product_data={"name": "Payments"},
    )

# Создание сессии для оплаты через Stripe
def create_stripe_session(price_id):
    """Создает сессию Stripe для получения ссылки на оплату."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        cancel_url="https://127.0.0.1:8000/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")