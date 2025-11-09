from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import VideoUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}
        validators = [VideoUrlValidator()]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    subscription = serializers.SerializerMethodField()

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()

    def get_subscription(self, instance):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return bool(Subscription.objects.filter(
                user=request.user,
                course=instance
            ))
        return False

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'preview', 'lessons_count', 'lessons', 'subscription')

        extra_kwargs = {'owner': {'read_only': True}}
