from django.shortcuts import render
from .models import Manual
from django.views.generic import ListView

class ManualListView(ListView):
    model = Manual
    template_name = 'manuals_page.html'
    context_object_name = 'manuals'