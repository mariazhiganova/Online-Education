from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, PaymentCreateAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('profile/<int:pk>/update/', UserUpdateAPIView.as_view(), name='profile_update'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment_list'),
]
