from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModel

User = get_user_model()


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"UID: {self.uid} | Name: {self.name}"


class OrganizationUser(BaseModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organization_users"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_organization"
    )

    def __str__(self):
        return (
            f"UID: {self.uid} | User: {self.user} | Organization: {self.organization}"
        )
