from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='index'),
    path('add/', views.add_purchase, name='add_purchase'),
    path('purchases/', views.list_purchases, name='list_purchases'),
    path('edit/<int:pk>/', views.edit_purchase, name='edit_purchase'),
    path('delete/<int:pk>/', views.delete_purchase, name='delete_purchase'),
]
