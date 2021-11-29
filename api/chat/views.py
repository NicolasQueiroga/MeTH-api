from .models import *
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response


# @permission_classes([IsAuthenticated])
class MessageViews(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            queryset = Message.objects.filter(user=(user))
        else:
            queryset = Message.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Artist Bookmark Deleted', status=status.HTTP_204_NO_CONTENT)
