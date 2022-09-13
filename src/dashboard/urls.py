from django.urls import path
from . import views

app_name   = 'dashboard'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('service', views.ServiceView.as_view(), name="service"),
    path('transaction', views.TransactionView.as_view(), name="transaction"),
    path('confirmation', views.ConfirmationView.as_view(), name="confirmation"),
    path('history', views.TransactionHistoryView.as_view(), name="history"),
    path('dashboard', views.DashboardOverviewView.as_view(), name="dashboard_overview"),
    path('dashboard/transaction', views.DashboardTransactionView.as_view(), name="dashboard_transaction"),
    path('dashboard/settings', views.DashboardSettingsView.as_view(), name="dashboard_settings"),
    path('verification', views.OTPVerification.as_view(), name="verification"),
    path('resendOTP', views.resend_OTP, name='resendOTP' )
]

