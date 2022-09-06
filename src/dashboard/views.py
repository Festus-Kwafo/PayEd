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
            otp_number = random.randint(100001, 999999)
            print(number)
            print(otp_number)
            #send_otp_sms(number, str(otp_number))
            return redirect('dashboard:verification')

        return redirect('dashboard:service')

class OTPVerification(View):
    template_name = 'templates/dashboard/otp.html'

    def get(self, request):

        return render(request, self.template_name)
        
    def post(self, request):
        otp_array = []
        if request.method == "POST":
            otp1 = request.POST.get('otp1') 
            otp2 = request.POST.get('otp2') 
            otp3 = request.POST.get('otp3') 
            otp4 = request.POST.get('otp4') 
            otp5 = request.POST.get('otp5') 
            otp6 = request.POST.get('otp6')
            otp_input = f'{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}'
            return redirect('dashboard:service')

class ServiceView(View):
    template_name = 'templates/dashboard/forms.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return redirect('dashboard:transaction')

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

