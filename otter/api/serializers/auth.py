from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from apps.organization.models import Organization, OrganizationUser
from apps.subscription.models import SubscriptionPlan

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "uid",
            "first_name",
            "last_name",
            "email",
            "password",
            "street_address",
            "city",
            "zip_code",
            "country",
            "time_zone",
        ]

        read_only_fields = ["uid", "time_zone"]

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return email

    def create(self, validated_data):
        with transaction.atomic():
            password = validated_data.pop("password")
            first_name = validated_data.get("first_name")
            last_name = validated_data.get("last_name")

            user = User(**validated_data)
            user.set_password(password)
            user.save()

            organization = Organization.objects.create(
                name=f"{first_name} {last_name}", dialog_api_key="test"
            )
            OrganizationUser.objects.create(user=user, organization=organization)
            SubscriptionPlan.objects.create(
                organization=organization, event_limit=1, invitation_limit=50
            )

            return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "first_name",
            "last_name",
            "email",
            "street_address",
            "city",
            "zip_code",
            "country",
            "time_zone",
        ]

        read_only_fields = ["uid", "time_zone"]

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return email
