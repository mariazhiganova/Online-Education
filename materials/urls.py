from django.urls import include, path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonDestroyAPIView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
                  path('lessons/list/', LessonListAPIView.as_view(), name='lessons_list'),
                  path('lessons/<int:pk>/update/', LessonListAPIView.as_view(), name='lessons_list'),
                  path('lessons/<int:pk>/details/', LessonRetrieveAPIView.as_view(), name='lessons_details'),
                  path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lessons_delete'),

              ] + router.urls
