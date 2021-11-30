from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('messages/<int:sender>/<int:receiver>/',
         MessageView.as_view(), name='get-messages'),
    path('messages/send/',
         MessageView.as_view(), name='send-message'),
]
