from django.urls import path
from main.views import show_main #biar klo ngeklik url muncul

urlpatterns = [
    path('', show_main, name='show_main'),
]
