from django.shortcuts import render
from app_full.models import Connections, Works, OurWorkers, OurTariffs
from django.views.generic import ListView, TemplateView


class HomePage(TemplateView):
    template_name = 'basic.html'



class ConnectionsList(ListView):
    model = Connections
    template_name = 'home.html'  # need rewrite
    context_object_name = 'messages'


class WorksList(ListView):
    model = Works
    template_name = 'works_list.html'   # need rewrrite
    context_object_name = 'works_list'


class OurWorkersList(ListView):
    model = OurWorkers
    template_name = 'workers_list.html'
    context_object_name = 'our_workers'


class OurTariffsList(ListView):
    model = OurTariffs
    template_name = 'tariffs_list.html'
    context_object_name = 'our_tariffs'


