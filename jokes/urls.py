from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListJokesView


urlpatterns = [
    path('joke-new/', ListJokesView.as_view(), name="jokes-all"),
]