from django.urls import path
from . import views

urlpatterns = [
    path('', views.factions_list, name='factions_list'),
    path('faction/<int:pk>/', views.faction_detail, name='faction_detail'),
path('dashboard/', views.dashboard, name='dashboard'),
]
