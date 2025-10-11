from rest_framework import generics
from users.models import AbstractUser
from users.serializers import UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = AbstractUser.objects.all()
    serializer_class = UserSerializer
