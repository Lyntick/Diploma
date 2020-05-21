from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import StatisticListSerializer
from .models import Statistic

class StatisticListView(generics.ListAPIView):
    serializer_class = StatisticListSerializer
    queryset = Statistic.objects.all()
    permission_classes = (IsAdminUser,)

