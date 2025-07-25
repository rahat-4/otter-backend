from django.urls import path

from ..views.auth import OrganizationUserOnboardView

urlpatterns = [
    path(
        "/onboard",
        OrganizationUserOnboardView.as_view(),
        name="organization_user_onboard",
    ),
]
