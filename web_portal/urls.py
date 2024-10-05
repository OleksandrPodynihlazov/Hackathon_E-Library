from django.urls import path
from .views import ManualListView, AccountDetailView, QuizListView

urlpatterns = [
    path('', ManualListView.as_view(), name='home'),
    path('quizzes/', QuizListView.as_view(), name='quiz_page'),
    path('accounts/details', AccountDetailView.as_view(), name='account'),
]