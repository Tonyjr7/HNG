from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import ME
from api.serializers import MESerializer

# Create your views here.
class ListME(generics.ListAPIView):
    queryset = ME.objects.all()
    serializer_class = MESerializer
    



