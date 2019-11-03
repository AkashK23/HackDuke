from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeContactView, ChangeAboutView, RideView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('contact/', ChangeContactView.as_view(), name='contact'),
    path('about/', ChangeAboutView.as_view(), name='about'),

    path('accounts/', include('accounts.urls')),
    path('user/', include('carpool.urls')),

    path('ride/', RideView.as_view(), name='ride')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
