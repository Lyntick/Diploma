from .serializers import ActiveDriveSerializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import ActiveDriver
from client.serializers import ActivePassengers, ClientSerializers
from django.db.models import Count, F


class ActiveDriverView(generics.CreateAPIView):
    serializer_class = ActiveDriveSerializers
    queryset = ActiveDriver.objects.all()
    permission_classes = (IsAuthenticated,)


class ActiveEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActiveDriveSerializers
    queryset = ActiveDriver.objects.all()
    permission_classes = (IsAuthenticated,)


class ActiveDriverGetPassgersToSit(generics.ListAPIView):  # доделать запрос, объекты выводятся, не работает подсчет количества объектов
    serializer_class = ClientSerializers

    def get_queryset(self):
        queryset = ActivePassengers.objects.all()
        index = self.request.query_params.get('idstop', None)
        if index is not None:
            queryset = queryset.raw('''SELECT * FROM public.client_activepassengers WHERE "idStop" = %s ''',[index])
#count?
        return queryset


class ActiveDriverGetPassgersToOut(
    generics.ListAPIView):  # доделать запрос, не работает подсчет количества объектов, объекты выводятся
    serializer_class = ActiveDriveSerializers

    def get_queryset(self):
        queryset = ActiveDriver.objects.all()
        index = self.request.query_params.get('iddriver', None)
        if index is not None:
            qs = queryset.filter(idDriver__exact=index)
            q = qs.filter(numberPassengers__ToStop__exact=F('Locate'))
            queryset = q.count()

        return queryset
