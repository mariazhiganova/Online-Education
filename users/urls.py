from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, PaymentCreateAPIView, PaymentListAPIView, UserCreateAPIView, \
    UserRetrieveAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='profile_register'),
    path('profile/<int:pk>/update/', UserUpdateAPIView.as_view(), name='profile_update'),
    path('profile/<int:pk>/details/', UserRetrieveAPIView.as_view(), name='profile_details'),
    path('profile/<int:pk>/delete/', UserDestroyAPIView.as_view(), name='profile_delete'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment_list'),

    path('login/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),

]
