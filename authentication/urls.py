from django.urls import path, include
from authentication.views import login, register

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('auth/', include('authentication.urls')),
    path('register/', register, name='register'),
]