from django.urls import path,include
from .views import HomePageView, ManualListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('/manuals/', ManualListView.as_view(), name='manuals_list'),
]
