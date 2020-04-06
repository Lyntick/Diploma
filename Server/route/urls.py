from django.contrib import admin
from django.urls import path, include
from route.views import StopListView

urlpatterns = [
    path('stop/all', StopListView.as_view())
]