from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import ME
from api.serializers import MESerializer

# Create your views here.
class ListME(generics.RetrieveAPIView):
    queryset = ME.objects.all()
    serializer_class = MESerializer

    def get_object(self):
        return ME.objects.last()  # Returns the latest ME entry

    



