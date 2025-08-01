from rest_framework import serializers

from apps.event.models import Event


class OrganizationEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "uid",
            "title",
            "start_date",
            "start_time",
            "location",
            "description",
            "invitation_link",
        ]
