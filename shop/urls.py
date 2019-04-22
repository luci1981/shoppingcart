from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_list, name='home'),
    path('category/<int:pk>/', views.product_list, name='products')
]