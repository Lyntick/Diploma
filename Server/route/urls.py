from django.contrib import admin
from django.urls import path, include
from route.views import StopListView, RouteListView, RouteDetailView

urlpatterns = [
    path('stop/all', StopListView.as_view()),
    path('route/all', RouteListView.as_view()),
    path('route/<int:pk>', RouteDetailView.as_view())
]
