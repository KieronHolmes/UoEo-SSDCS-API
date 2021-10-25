"""
The URLs to be used under the /api/v1/microservice/ prefix.
"""
from django.urls import path

from .views import MicroserviceSearchView

urlpatterns = [
    path("<str:query>", MicroserviceSearchView.as_view(), name="microservice_search")
]
