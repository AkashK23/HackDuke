from django.urls import path

from . import views

app_name = "carpool"
urlpatterns = [
    path('<user>', views.IndexView.as_view(), name='index'),
    path('<user>/', views.IndexView.as_view(), name='index'),
    path('<user>/driverform', views.DriverForm.as_view(), name='driverform'),
    path('<user>/passengerform', views.PassengerForm.as_view(), name='passengerform')
]
