from django.urls import path
from .views import dashboard, run_manual_check, toggle_auto_monitor

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('check/<int:pk>/', run_manual_check, name='run_manual_check'),
    path('toggle/<int:pk>/', toggle_auto_monitor, name='toggle_auto_monitor'),
]