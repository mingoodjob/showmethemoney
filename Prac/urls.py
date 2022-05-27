from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.base),
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
]
