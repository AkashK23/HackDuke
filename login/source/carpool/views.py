from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import User
from django import forms
from django.forms.widgets import DateTimeInput
from django.urls import reverse

class IndexView(TemplateView):
    template_name = "main/profile.html"
    context_object_name = "drivers"

    def get_queryset(self):
        # Need to select backend
        return User.objects.all()

class DriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["mpg", "capacity", "destination", "source", "departure_time"]
        # departure_time: 'Example: 1/1/1000 1:11'
        exclude = ["user"]
        widgets = {
            'departure_time': DateTimeInput(attrs={
                'class': 'datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        }

class DriverForm(CreateView):
    form_class = DriverForm
    model = User
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