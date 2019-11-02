from django.urls import path

from .views import *

urlpatterns = [
    path('movieOnInfoList', get_movieOnInfoList),
    path('comingList', get_comingList),
    path('cinemaList', get_cinemaList)
]
