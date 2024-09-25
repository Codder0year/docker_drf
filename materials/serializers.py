from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validate_youtube_link], required=False)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("name", "lessons_count", "lesson_list", "is_subscribed")

    def get_lessons_count(self, obj):
        return obj.lesson_set.filter().count()

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user

        # Проверка, подписан ли пользователь на курс
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'course']
