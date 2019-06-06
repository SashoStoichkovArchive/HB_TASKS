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


def details(request, plane_name):
    template = loader.get_template('planes/index.html')
    planes = models.Plane.objects.filter(name=plane_name)
    if len(planes) == 0:
        raise models.Plane.DoesNotExist
    context = {
        'planes': planes
    }
    # res = template.render()
    print(planes)
    # return HttpResponse(res)
    return render(request, 'planes/index.html', context)


def flights(request):
    all_flights = models.Flight.objects\
        .all()\
        .select_related('user', 'plane')

    template_context = {
        'flights': all_flights
    }

    return render(request, 'planes/list_flights.html', template_context)



def create_flight(request):
    errors = None

    form = FlightForm()

    if request.method == 'POST':
        data = request.POST
        form = FlightForm(data=data)
        if not form.is_valid():
            errors = form.errors

        cleaned_data = form.cleaned_data

        plane = models.Plane.objects.get(id=cleaned_data['plane'])
        user = User.objects.get(id=cleaned_data['user'])

        models.Flight.objects.create(
            start_time=cleaned_data['start_time'],
            end_time=cleaned_data['end_time'],
            passengers=cleaned_data['passengers'],
            max_passengers=cleaned_data['max_passengers'],
            from_dest=cleaned_data['from_dest'],
            to_dest=cleaned_data['to_dest'],
            plane=plane,
            user=user,
        )

    return render(
        request,
        'planes/create_flight.html',
        {'errors': errors, 'form': form}
    )

class CreateFlightView(View):
    def get(self, request):
        form = FlightForm()
        print('GEEEET')
        return render(
            request,
            'planes/create_flight.html',
            {'form': form}
        )

    def post(self, request):
        print('POST')
        errors = None

        data = request.POST
        form = FlightForm(data=data)
        if not form.is_valid():
            errors = form.errors
        else:
            cleaned_data = form.cleaned_data

            models.Flight.objects.create(
                start_time=cleaned_data['start_time'],
                end_time=cleaned_data['end_time'],
                passengers=cleaned_data['passengers'],
                max_passengers=cleaned_data['max_passengers'],
                from_dest=cleaned_data['from_dest'],
                to_dest=cleaned_data['to_dest'],
                plane=cleaned_data['plane'],
                user=cleaned_data['user'],
            )

        return render(
            request,
            'planes/create_flight.html',
            {'errors': errors, 'form': form}
        )

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