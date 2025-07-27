from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, UpdateAPIView

from apps.organization.models import OrganizationUser

from ..serializers.auth import UserRegistrationSerializer, UserProfileSerializer


User = get_user_model()


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = []


class UserProfileView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        user_uid = self.kwargs.get("user_uid")
        return User.objects.get(uid=user_uid)
