from django.urls import path

from users.views import UserUpdateAPIView

urlpatterns = [
    path('profile/<int:pk>/update/', UserUpdateAPIView.as_view(), name='profile_update'),
]
