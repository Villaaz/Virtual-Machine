from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pagar/', views.pagar, name='pagar'),
    path('edit/<int:pk>/', views.edit_producto.as_view(), name='edit-producto'),
]