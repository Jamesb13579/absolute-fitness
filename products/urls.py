from django.urls import path
from . import views


urlpatterns = [
    path('', views.products, name='products'),
    path('memberships/', views.memberships, name='memberships'),
]