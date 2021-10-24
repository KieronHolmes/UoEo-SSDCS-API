"""
The URLs to be used under the /api/v1/documents/ prefix.
"""
from django.urls import path

from .views import DocumentDetailView, DocumentList

urlpatterns = [
    path('', DocumentList.as_view()),
    path('<str:id>', DocumentDetailView.as_view())
]
