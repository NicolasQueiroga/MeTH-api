from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail


class EmailSendView(APIView):
    def post(self, request, format=None):
        send_mail(request.data['subject'], request.data['body'],
                  'noreply.suporte.meth@gmail.com',
                  ['noreply.receptor.meth@gmail.com'])
        return Response(request.data, status=status.HTTP_201_CREATED)
