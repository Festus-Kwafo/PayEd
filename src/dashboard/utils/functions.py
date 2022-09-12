import requests 
from core.settings import SMS_APIKEY
from django.utils.html import strip_tags

def get_errors_from_form(forms):
    error =[]
    for field, er in forms.errors.items():
        title = field.title().replace("_", " ")
        error.append(f"{title}: {strip_tags(er)}")
        return "".join(error)

def send_otp_sms(receiver, otp_number):
    endPoint = 'https://api.mnotify.com/api/sms/quick'
    #apiKey = 'K0SLuMX4M2SIL1FDVet05b8iCCJs15FM6xxAkuE6wwPiy'
    apiKey = SMS_APIKEY
    data = {
   'recipient[]': [receiver],
   'sender': 'PayEd',
   'message': f'{otp_number} is PayEd verifaction Code. Don\'t share this code',
   'is_schedule': False,
            }
    url = endPoint + '?key=' + str(apiKey)
    response = requests.post(url, data)
    data = response.json()
    print(data)
    return response.json()
