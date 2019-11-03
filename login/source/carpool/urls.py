from django.urls import path

from . import views

urlpatterns = [
    path('<user>', views.IndexView.as_view(), name='index'),
]
