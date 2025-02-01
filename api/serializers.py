from rest_framework import serializers
from .models import ME
from django.utils import timezone

class MESerializer(serializers.ModelSerializer):

    current_datetime = serializers.SerializerMethodField()
    
    class Meta:
        model = ME
        fields = ['email', 'current_datetime', 'github_url']

 def get_current_datetime(self, obj):
        return timezone.now()
