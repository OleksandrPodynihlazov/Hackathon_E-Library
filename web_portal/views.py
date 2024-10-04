from .models import Manual
from django.views.generic import ListView,  TemplateView

class ManualListView(ListView):
    model = Manual
    template_name = 'manuals_page.html'
    context_object_name = 'manuals'

class HomePageView(TemplateView):
    template_name = 'home.html'
