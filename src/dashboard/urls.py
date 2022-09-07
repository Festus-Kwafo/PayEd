from django.urls import path
from . import views

app_name   = 'dashboard'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('service', views.ServiceView.as_view(), name="service"),
    path('transaction', views.TransactionView.as_view(), name="transaction"),
    path('confirmation', views.ConfirmationView.as_view(), name="confirmation"),
    path('history', views.TransactionHistoryView.as_view(), name="history"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard"),
    path('verification/<str:number>/', views.OTPVerification.as_view(), name="verification"),
]

