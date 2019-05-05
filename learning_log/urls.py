from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls', namespace='learning_logs')),
    path('users/', include('users.urls', namespace='users')),
]
