from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:pk>', views.ContentDetailListView.as_view(), name='content'),  # Замість ContentView поставте своє представлення
    path('save_link/', views.save_link, name='save_link'),  # представлення для збереження посилання
]
