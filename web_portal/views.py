from .models import Manual
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class ManualListView(LoginRequiredMixin, ListView):
    model = Manual
    template_name = 'manuals_page.html'
    context_object_name = 'manuals'

class AccountDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'
    context_object_name = 'account'

class ManualDetailView(LoginRequiredMixin, DetailView):
    model = Manual
    template_name = 'manual.html'
    context_object_name = 'manual'
