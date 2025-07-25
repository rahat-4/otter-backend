from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.organization.models import Organization, OrganizationUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        errors = {}
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            errors["email"] = "User with this email already exists."

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["uid", "name", "description"]

    def validate(self, attrs):
        errors = {}
        name = attrs.get("name")
        if Organization.objects.filter(name=name).exists():
            errors["name"] = "Organization with this name already exists."

        return attrs


class OrganizationUserOnboardSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = OrganizationUser
        fields = ["uid", "organization", "user"]

    def validate(self, attrs):
        errors = {}
        user = attrs.get("user")
        organization = attrs.get("organization")

        if OrganizationUser.objects.filter(
            user=user, organization=organization
        ).exists():
            errors["user"] = "User is already a member of this organization."

        return attrs
