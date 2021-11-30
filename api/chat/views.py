from rest_framework.views import APIView
from .models import *
from .serializers import *
from .models import Message
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from operator import attrgetter
from itertools import chain


@permission_classes([IsAuthenticated])
class MessageView(APIView):
    def get(self, request, sender=None, receiver=None):
        messages_sender = Message.objects.filter(
            sender_id=sender, receiver_id=receiver)
        messages_receiver = Message.objects.filter(
            sender_id=receiver, receiver_id=sender)
        for message in messages_receiver:
            message.is_read = True
            message.save()
        messages = sorted(
            chain(messages_sender, messages_receiver),
            key=attrgetter('timestamp'))
        serializer = MessageSerializer(
            messages, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
