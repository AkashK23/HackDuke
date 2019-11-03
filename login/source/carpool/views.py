from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, FormView
from .models import User
from django import forms
from django.forms.widgets import DateTimeInput
from django.urls import reverse

class IndexView(TemplateView):
    template_name = "main/profile.html"

class DriverInput(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user", "mpg", "capacity", "destination", "source", "departure_time"]
        widgets = {
            'departure_time': DateTimeInput(attrs={
                'class': 'datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        }

class DriverForm(CreateView):
    model = User
    template_name = "main/form.html"
    fields = ["user", "mpg", "capacity", "destination", "source", "departure_time"]
    labels = {"departure_time": 'Example: 1/1/1000 1:11'}

    def get_success_url(self):
        return reverse('ride')

class PassengerForm(CreateView):
    model = User
    fields = ["user", "destination", "source", "departure_time"]
    exclude = ["mpg", "capacity"]
    template_name = "main/form.html"

    def get_success_url(self):
        return reverse('ride')