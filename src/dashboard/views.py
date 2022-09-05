from django.shortcuts import render, redirect
from django.views import View
import random
from .utils.functions import send_otp_sms

# Create your views here.
class IndexView(View):
    template_name = 'templates/dashboard/index.html'


    def get(self, request):

        return render(request, self.template_name)
    def post(self, request):
        if request.method == "POST":
            print("Yess")
            number = request.POST.get('phoneNumber')
            otp_number = random.randint(0, 9999)
            print(type(number))
            print(type(str(otp_number)))
            send_otp_sms(number, str(otp_number))
            return render(request, 'templates/dashboard/otp.html')
        return redirect('dashboard:service')

class ServiceView(View):
    template_name = 'templates/dashboard/forms.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return redirect('dashboard:')

class TransactionView(View):
    template_name = "templates/dashboard/transaction.html"

    def get(self, request):
        return render(request, self.template_name)

class ConfirmationView(View):
    template_name = 'templates/dashboard/payment_confirmation.html'

    def get(self, request):
        return render(request, self.template_name)

class TransactionHistoryView(View):
    template_name = 'templates/dashboard/transaction_history.html'

    def get(self, request):
        return render(request, self.template_name)
class DashboardView(View):
    template_name = 'templates/dashboard/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

