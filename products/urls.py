from django.urls import path
from . import views


urlpatterns = [
    path('', views.products, name='products'),
    path('memberships/', views.memberships, name='memberships'),
    path('<product_id>/', views.product_detail, name='product_detail'),
]