from django.urls import path
from .views import ManualListView, AccountDetailView, ManualDetailView, QuizListView

urlpatterns = [
    path('', ManualListView.as_view(), name='home'),
    path('accounts/details', AccountDetailView.as_view(), name='account'),
    path('manuals/<int:pk>', ManualDetailView.as_view(), name='manual'),
    path('quizzes/', QuizListView.as_view(), name='quiz_page'),
]