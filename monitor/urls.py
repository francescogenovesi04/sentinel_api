from django.urls import path
from .views import dashboard, run_manual_check

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('check/<int:pk>/', run_manual_check, name='run_manual_check'),
]