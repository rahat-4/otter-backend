from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView

from apps.event.models import Event
from apps.organization.models import Organization, OrganizationUser

from apps.subscription.choices import SubscriptionType

from ..serializers.organizations import OrganizationEventSerializer


class OrganizationEventListView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = OrganizationEventSerializer

    def get_queryset(self):
        organization_uid = self.kwargs.get("organization_uid")
        return Event.objects.filter(organization__uid=organization_uid)

    def perform_create(self, serializer):
        organization_uid = self.kwargs.get("organization_uid")
        organization = Organization.objects.get(uid=organization_uid)

        # Get the subscription plan for this organization
        subscription_plan = organization.organizations_subscription_plan

        if subscription_plan.subscription_type == SubscriptionType.FREE:
            # Count existing events
            event_count = Event.objects.filter(organization=organization).count()

            if event_count >= subscription_plan.event_limit:
                raise PermissionDenied("FREE plan allows only one event.")

        serializer.save(organization=organization)
