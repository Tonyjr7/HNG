from django.shortcuts import render
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import generics
from .models import ME
from api.serializers import MESerializer

# Create your views here.
class ListME(generics.ListAPIView):
    queryset = ME.objects.all()
    serializer_class = MESerializer

    def list(self, request, *args, **kwargs):
        # Get the current datetime for every request
        current_time = timezone.now()

        # Get the default response data
        response = super().list(request, *args, **kwargs)
        
        # Add the current time to the response data
        response.data.append({"current_datetime": current_time})  # Add real-time current time to the response

        return response
    



