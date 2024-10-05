from django.urls import path
from .views import HomePageView, ManualListView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', ManualListView.as_view(), name='manuals_list'),
]
