from django.urls import path, include
from email.views import EmailSendView

urlpatterns = [
    path('send/', EmailSendView.as_view(), name='sendEmail'),
]