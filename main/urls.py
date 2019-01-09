from django.urls import path
from .views import wszystkie_filmy

urlpatterns = [
    path('filmy/', wszystkie_filmy),
]