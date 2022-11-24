from django.urls import path
from . import views


urlpatterns = [
    path('trainers/', views.trainers, name='trainers'),
    path('classes/', views.classes, name='classes'),
    path('gym/', views.gym, name='gym'),
]
