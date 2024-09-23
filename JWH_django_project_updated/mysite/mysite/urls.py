from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', views.current_time, name='current_time'),
    path('', views.home, name='home'),
]
