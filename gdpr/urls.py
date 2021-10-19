from django.urls import path

from .views import SubjectAccessRequestView, SubjectErasureRequestView

urlpatterns = [
    path(
        "access-request/",
        SubjectAccessRequestView.as_view({"get": "list"}),
        name="subject_access_request",
    ),
    path(
        "erasure-request/",
        SubjectErasureRequestView.as_view(),
        name="subject_access_request",
    ),
]
