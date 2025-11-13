from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import CustomUser


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@mail.com', password='testuser123')
        self.course = Course.objects.create(title='test course 1', description='test course', owner=self.user)
        self.existing_lesson_1 = Lesson.objects.create(
            title="Existing lesson",
            description='test lesson',
            video_url='https://youtu.be/test/',
            course=self.course,
            owner=self.user
        )
        self.existing_lesson_2 = Lesson.objects.create(
            title='Existing lesson 2',
            description='test lesson 2',
            video_url='https://youtu.be/test/2/',
            course=self.course,
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {
            'title': 'New lesson',
            'description': 'New test lesson',
            'video_url': 'https://youtu.be/test/1/',
            'course': self.course.id
        }

        response = self.client.post(
            reverse('materials:lessons_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        """Тестирование просмотра одного урока"""
        response = self.client.get(
            reverse('materials:lessons_details', kwargs={'pk': self.existing_lesson_1.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        """Тестирование обновления урока"""
        data = {
            'video_url': 'https://youtu.be/test/2/new/'
        }
        response = self.client.patch(
            reverse('materials:lessons_update', kwargs={'pk': self.existing_lesson_2.id}),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_lesson(self):
        """Тестирование просмотра списка уроков"""
        response = self.client.get(
            reverse('materials:lessons_list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_delete(self):
        """Тестирование удаления урока"""
        response = self.client.delete(
            reverse('materials:lessons_delete', kwargs={'pk': self.existing_lesson_2.id})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_subscription(self):
        """Тестирование подписки на курс"""
        data = {
            'course_id': self.course.id
        }
        response = self.client.post(
            reverse('materials:course_subscription'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
