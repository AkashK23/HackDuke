from django.urls import path

from . import views

urlpatterns = [
    path('<user>', views.IndexView.as_view(), name='index'),
    path('<user>/driverform', views.DriverForm.as_view(), name='driverform'),
    path('<user>/passengerform', views.PassengerForm.as_view(), name='passengerform')
]
