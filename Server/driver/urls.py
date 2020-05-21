from django.conf.urls import url
from django.urls import path, include
from django import urls
from .views import ActiveDriverView, ActiveDriverGetPassgersToSit, ActiveEditView , ActiveDriverGetPassgersToOut

urlpatterns = [
    url('^active/sit/(?P<idstop>)$', ActiveDriverGetPassgersToSit.as_view()),
    path('active/create/', ActiveDriverView.as_view()),
    path('active/edit/<int:pk>/', ActiveEditView.as_view()),
    url('^active/out/(?P<iddriver>)$', ActiveDriverGetPassgersToOut.as_view()),
]
