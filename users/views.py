from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import CustomUser, Payment
from users.permissions import IsOwner
from users.serializers import PaymentSerializer, UserPublicSerializer, UserPrivateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserPublicSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        user = serializer.save(is_active=True)
        user.set_password(password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserPrivateSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwner]

    def get_serializer_class(self):
        if self.get_object() == self.request.user:
            return UserPrivateSerializer
        return UserPublicSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwner]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_time']
