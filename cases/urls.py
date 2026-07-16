from django.urls import path
from .views import case_detail, client_cases, lawyer_cases

urlpatterns = [
    path('my-cases/', client_cases, name='client_cases'),
    path('lawyer-cases/', lawyer_cases, name='lawyer_cases'),
    path('detail/<int:case_id>/', case_detail, name='case_detail'),
]