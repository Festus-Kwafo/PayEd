from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.
class Sms(models.Model):
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()
    number = models.CharField(max_length=10)
    response = models.TextField()
    status_message = models.TextField(null=True, blank=True)
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    otp_number = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "SMS"
        verbose_name_plural = "SMS's"

    def save(self, *args, **kwargs ):
        if not self.subject:
            self.subject == self.message[:50]
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.message
