from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from .forms import FlightForm
from . import models


# Create your views here.
def index(request):
    template = loader.get_template('planes/index.html')
    planes = models.Plane.objects.all().order_by('-capacity')
    context = {
        'planes': planes
    }
    # res = template.render()
    print(planes)
    # return HttpResponse(res)
    return render(request, 'planes/index.html', context)

from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView


from django.contrib.auth.views import LoginView

class CreateFlightCreateView(CreateView):
    model = models.Flight
    fields = '__all__'
    template_name = 'planes/create.html'



class UpdateFlightUpdateView(UpdateView):
    model = models.Flight
    fields = '__all__'
    template_name = 'planes/update.html'
    success_url = reverse_lazy('flights')


class DetailFlightDetailView(DetailView):
    model = models.Flight
    template_name = 'planes/detail.html'


class DeleteFlightDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Flight
    template_name = 'planes/delete.html'
    success_url = reverse_lazy('flights')


class ListFlightListView(ListView):
    model = models.Flight
    template_name = 'planes/list.html'

class UserLoginView(LoginView):
    template_name = 'planes/user_login.html'
