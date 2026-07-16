from django.urls import path
from .views import client_dashboard, lawyer_dashboard, register_view , login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('lawyer-dashboard/', lawyer_dashboard, name='lawyer_dashboard'),
    path('client-dashboard/', client_dashboard, name='client_dashboard'),
]