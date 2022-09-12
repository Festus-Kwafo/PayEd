from dataclasses import field
from .models import Sms
from django import forms

class SmsForm(forms.ModelForm):
    class Meta:
        model = Sms
        exclude = [
            'id',
            'subject',
            'message',
            'response',
            'status_message',
            'success',
            'created_at',
            'update_at',
            'otp_number',
            'verified'
        ]