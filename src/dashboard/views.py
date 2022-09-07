from multiprocessing import context
import re
from django.shortcuts import render, redirect 
from django.views import View
from django.urls import reverse
import random
from django.http import HttpResponseRedirect

from dashboard.models import Sms
from .utils.functions import send_otp_sms, get_errors_from_form
from .forms import SmsForm
from django.contrib import messages

# Create your views here.
class IndexView(View):
    template_name = 'templates/dashboard/index.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        forms = SmsForm(request.POST)
        # if request.method == "POST":
        sms_model = Sms()       
        if forms.is_valid():
            otp_number = random.randint(100001, 999999)
            number = request.POST.get('number')
            print(number)
            is_number_exists = Sms.objects.filter(number=number).exists()
            if is_number_exists:
                sms_number = Sms.objects.filter(number=number).update(otp_number=otp_number)
                #send sms to valid number
            else:
                sms_number = Sms.objects.create(
                    number = number,
                    otp_number = otp_number
                )
            #send_otp_sms(number, str(otp_number))
            context = {
                'number': number
            }
            
            return HttpResponseRedirect(reverse('dashboard:verification', kwargs={'number':number}))
                
        else:
            error_message = get_errors_from_form(forms)
            messages.warning(request, error_message)
            return redirect('dashboard:home')




class OTPVerification(View):
    template_name = 'templates/dashboard/otp.html'

    def get(self, request, *args, **kwargs):
        number = kwargs.get('number')
        context = {
            'number': number
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        sms_verify = Sms.objects.get(number = self.kwargs['number'])
        otp1 = request.POST.get('otp1') 
        otp2 = request.POST.get('otp2') 
        otp3 = request.POST.get('otp3') 
        otp4 = request.POST.get('otp4') 
        otp5 = request.POST.get('otp5') 
        otp6 = request.POST.get('otp6')
        print(sms_verify.otp_number)
        otp_input = f'{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}'
        if sms_verify.otp_number == otp_input.strip():
            print("True")
            return redirect('dashboard:service')
        else:
            messages.warning(request, "OTP does not match")
            return HttpResponseRedirect(reverse('dashboard:verification', kwargs={'number': self.kwargs['number']}))
        

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

