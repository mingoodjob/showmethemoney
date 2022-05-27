from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.sign_up, name='sign_up'),
]