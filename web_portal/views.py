from .models import Manual, Quiz
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ManualListView(LoginRequiredMixin, ListView):
    model = Manual
    template_name = 'manuals_page.html'
    context_object_name = 'manuals'

class AccountDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'
    context_object_name = 'account'

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_page.html'  # ваш шаблон
    context_object_name = 'quizzes' 