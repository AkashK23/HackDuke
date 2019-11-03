from django.views.generic import TemplateView, CreateView, ListView
from carpool.models import User

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeContactView(TemplateView):
    template_name = 'main/contact.html'

class ChangeAboutView(TemplateView):
    template_name = 'main/about.html'

class RideView(ListView):
    template_name = "main/ride.html"
    context_object_name = "drivers"
    
    def get_queryset(self):
        data = User.objects.all()
        if data.exists():
            for u in data.iterator():
                print(u.destination)
        return User.objects.all()