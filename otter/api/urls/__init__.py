from django.urls import path, include


urlpatterns = [
    path("/auth", include("api.urls.auth")),
    path("/organization", include("api.urls.organizations")),
]
