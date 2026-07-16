from django.urls import path
from .views import accept_request, create_request , lawyer_requests

urlpatterns = [
    path('create/', create_request, name='create_request'),
    path('lawyer/', lawyer_requests, name='lawyer_requests'),
    path('accept/<int:request_id>/', accept_request, name='accept_request'),
]