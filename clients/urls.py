from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListCreateView.as_view(), name='client-list'),
    path('<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('<int:client_id>/conflict-check/', views.ConflictCheckView.as_view(), name='conflict-check'),
    path('stats/', views.ClientStatsView.as_view(), name='client-stats'),
]