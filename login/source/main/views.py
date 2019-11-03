from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeContactView(TemplateView):
    template_name = 'main/contact.html'

class ChangeAboutView(TemplateView):
    template_name = 'main/about.html'

class RideView(TemplateView):
    template_name = "main/ride.html"