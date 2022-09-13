from django.http import HttpResponse
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
             
        if forms.is_valid():
            otp_number = random.randint(100001, 999999)
            number = request.POST.get('number')

            is_number_exists = Sms.objects.filter(number=number).exists()
            if is_number_exists:
                sms_number = Sms.objects.filter(number=number).update(otp_number=otp_number, verified=False)
            else:
                sms_number = Sms.objects.create(
                    number = number,
                    otp_number = otp_number
                )
            response = send_otp_sms(number, str(otp_number))
            sms_model = Sms.objects.get(number= number)
            sms_model.status_message = response['message']
            #save number in the session
            request.session['session_number'] = f'{number}' 
            sms_model.save()
            return redirect('dashboard:verification')
                
        else:
            error_message = get_errors_from_form(forms)
            messages.warning(request, error_message)
            return redirect('dashboard:home')




class OTPVerification(View):
    template_name = 'templates/dashboard/otp.html'

    def get(self, request):

        return render(request, self.template_name)
        
    def post(self, request, ):
        sms_verify = Sms.objects.get(number = request.session.get('session_number'))
        otp1 = request.POST.get('otp1') 
        otp2 = request.POST.get('otp2') 
        otp3 = request.POST.get('otp3') 
        otp4 = request.POST.get('otp4') 
        otp5 = request.POST.get('otp5') 
        otp6 = request.POST.get('otp6')


        #Compare otp entered by user to the OTP sent to the user and verify the user
        otp_input = f'{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}'
        if sms_verify.otp_number == otp_input.strip():
            sms_verify.verified = True
            sms_verify.save()
            return redirect('dashboard:service')

        else:
            messages.warning(request, "OTP does not match")
            return redirect('dashboard:home')
 
 #resend OTP function       
def resend_OTP(request):
    number = request.session.get('session_number')
    print(type(number))
    otp_number = random.randint(100001, 999999)
    Sms.objects.filter(number = number).update(otp_number=otp_number)
    response = send_otp_sms(number, str(otp_number))
    if response['status'] == 'success':
        messages.success(request, "OTP Sent successfully")
        return redirect('dashboard:verification')
    else:
        messages.warning(request, "Error Sending sending OTP. Try again later")
        return redirect('dashboard:home')

class ServiceView(View):
    template_name = 'templates/dashboard/forms.html'

    def get(self, request):
        
        session_number = request.session.get('session_number')
        is_number_verified = Sms.objects.filter(number = session_number, verified=True).exists()
        if is_number_verified:
            return render(request, self.template_name)
        else:
            messages.warning(request, "Login Required")
            return redirect('dashboard:home')
    
    def post(self, request):
        return redirect('dashboard:transaction')

class TransactionView(View):
    template_name = "templates/dashboard/transaction.html"

    def get(self, request):
        request.session['session_number']
        session_number = request.session['session_number']
        is_number_verified = Sms.objects.filter(number = session_number, verified=True).exists()
        if is_number_verified:
            return render(request, self.template_name)
        else:
            messages.warning(request, "Login Required")
            return redirect('dashboard:home')

class ConfirmationView(View):
    template_name = 'templates/dashboard/payment_confirmation.html'

    def get(self, request):
        session_number = request.session['session_number']
        is_number_verified = Sms.objects.filter(number = session_number, verified=True).exists()
        if is_number_verified:


            return render(request, self.template_name)

        else:
            messages.warning(request, "Login Required")
            return redirect('dashboard:home')

class TransactionHistoryView(View):
    template_name = 'templates/dashboard/transaction_history.html'

    def get(self, request):
        session_number = request.session['session_number']
        is_number_verified = Sms.objects.filter(number = session_number, verified=True).exists()
        if is_number_verified:
            return render(request, self.template_name)
        else:
            messages.warning(request, "Login Required")
            return redirect('dashboard:home')

class DashboardOverviewView(View):
    template_name = 'templates/dashboard/dashboard_overview.html'

    def get(self, request):
        return render(request, self.template_name)

class DashboardSettingsView(View):
    template_name = 'templates/dashboard/dashboard_settings.html'

    def get(self, request):
        return render(request, self.template_name)
        
class DashboardTransactionView(View):
    template_name = 'templates/dashboard/dashboard_transaction.html'

    def get(self, request):
        return render(request, self.template_name)

