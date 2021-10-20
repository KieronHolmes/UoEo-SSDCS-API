from django.urls import path

from .views import MicroserviceSearchView

urlpatterns = [
    path('<str:query>', MicroserviceSearchView.as_view(), name="microservice_search")
]
