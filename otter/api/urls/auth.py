from django.urls import path

from ..views.auth import UserRegistrationView, UserProfileView

urlpatterns = [
    path(
        "/<uuid:user_uid>/profile",
        UserProfileView.as_view(),
        name="user_profile",
    ),
    path(
        "/registration",
        UserRegistrationView.as_view(),
        name="user_registration",
    ),
]
