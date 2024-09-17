from rest_framework import serializers

from materials.models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = ("name", "lessons_count", "lesson_list")

    def get_lessons_count(self, obj):
        return obj.lesson_set.filter().count()

    # def get_lesson_list(self, obj):
    #     lessons = obj.lesson_set.all()
    #     serializer = LessonSerializer(lessons, many=True)
    #     return [lesson['name'] for lesson in serializer.data]

