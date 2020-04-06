from django.shortcuts import render
from rest_framework import generics
from Server.route.serializers import StopListSerializer, RouteListSerializer
from Server.route.models import Stop, Route


class StopListView(generics.ListAPIView):
    serializer_class = StopListSerializer
    queryset = Stop.objects.all()
