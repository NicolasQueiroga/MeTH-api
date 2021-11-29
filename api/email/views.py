from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmailSendView(APIView):
	"""
    API to send suport Emails
    """
        def post(self, request, format=None):
            print(request.data)
            return Response(request.data, status=status.HTTP_201_CREATED)