from django.urls import path
from .views import (ConnectionsList, WorksList, 
                    OurWorkersList, OurTariffsList,
                    HomePage)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('connections/', ConnectionsList.as_view(), name='connections'),
    path('works/', WorksList.as_view(), name='works'),
    path('workers/', OurWorkersList.as_view(), name='workers'),
    path('tariffs/', OurTariffsList.as_view(), name='tariffs'),
]