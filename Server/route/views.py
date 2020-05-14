from django.shortcuts import render
from rest_framework import generics
from route.serializers import StopListSerializer, RouteListSerializer
from route.models import Stop, Route
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StopListView(generics.ListAPIView):
    serializer_class = StopListSerializer
    queryset = Stop.objects.all()
    permission_classes = (IsAuthenticated,)# Если пользователь авторизован
    authentication_classes = (JWTAuthentication,)  # аутентификаци тольок с jwt токена


class RouteListView(generics.ListAPIView):
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


class RouteDetailView(generics.RetrieveAPIView):
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)