from django.urls import path
from .views import ManualListView, AccountDetailView, ManualDetailView

urlpatterns = [
    path('', ManualListView.as_view(), name='home'),
    path('manuals/<int:pk>/', ManualDetailView.as_view(), name='manual'),
    path('accounts/details', AccountDetailView.as_view(), name='account'),
]
