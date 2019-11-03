from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import User
from django import forms
from django.forms.widgets import DateTimeInput
from django.urls import reverse

class IndexView(TemplateView):
    template_name = "main/profile.html"

class DriverForm(CreateView):
    model = User
    fields = ["mpg", "capacity", "destination", "source", "departure_time"]
    exclude = ["user"]
    template_name = "main/form.html"

    def get_success_url(self):
        return reverse("index")

class PassengerForm(CreateView):
    model = User
    fields = ["destination", "source", "departure_time"]
    exclude = ["mpg", "capacity", "user"]
    template_name = "main/form.html"

    def get_success_url(self):
        return reverse("index")