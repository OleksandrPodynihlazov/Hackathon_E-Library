from django.urls import path
from .views import ManualListView, AccountDetailView

urlpatterns = [
    path('', ManualListView.as_view(), name='home'),
    path('accounts/details', AccountDetailView.as_view(), name='account'),
]
