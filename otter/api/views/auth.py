from rest_framework.generics import CreateAPIView

from apps.organization.models import OrganizationUser

from ..serializers.auth import OrganizationUserOnboardSerializer


class OrganizationUserOnboardView(CreateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserOnboardSerializer
