from rest_framework.generics import ListCreateAPIView

from apps.event.models import Event
from apps.organization.models import Organization, OrganizationUser

from ..serializers.organizations import OrganizationEventSerializer


class OrganizationEventListView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = OrganizationEventSerializer

    def perform_create(self, serializer):
        organization_uid = self.kwargs.get("organization_uid")
        organization = Organization.objects.get(uid=organization_uid)
        serializer.save(organization=organization)

    def get_queryset(self):
        organization_uid = self.kwargs.get("organization_uid")
        return Event.objects.filter(organization__uid=organization_uid)
