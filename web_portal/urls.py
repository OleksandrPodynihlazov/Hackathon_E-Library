from django.urls import path
from .views import ManualListView

urlpatterns = [
    path('', ManualListView.as_view(), name='manuals_list'),
]
