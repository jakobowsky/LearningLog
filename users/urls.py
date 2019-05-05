from django.urls import path
from django.contrib.auth.views import LoginView

from .views import logout_view, register


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(),
         {'template_name': 'users/login.html'}, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
