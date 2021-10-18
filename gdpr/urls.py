from django.urls import path
from .views import SubjectAccessRequestView

urlpatterns = [
    path("access-request/", SubjectAccessRequestView.as_view({'get': 'list'}), name="subject_access_request"),
]
