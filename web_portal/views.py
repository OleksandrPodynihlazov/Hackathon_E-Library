from .models import Manual
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ManualListView(LoginRequiredMixin, ListView):
    model = Manual
    template_name = 'manuals_page.html'
    context_object_name = 'manuals'

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
