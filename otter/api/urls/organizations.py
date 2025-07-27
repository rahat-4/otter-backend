from django.urls import path

from ..views.organizations import OrganizationEventListView

urlpatterns = [
    path(
        "/<uuid:organization_uid>/events",
        OrganizationEventListView.as_view(),
        name="event_list",
    ),
]
