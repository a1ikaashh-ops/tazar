from django.urls import path
from . import views

urlpatterns = [
    path('ecomap/', views.ecomap_view, name='ecomap'),
    path('ecomap/add/', views.add_point, name='add_point'),
    path('ecomap/delete/<int:pk>/', views.delete_point, name='delete_point'),
]