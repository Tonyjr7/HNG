from rest_framework import serializers
from .models import ME

class MESerializer(serializers.ModelSerializer):
    class Meta:
        model = ME
        fields = ['email', 'current_datetime', 'github_url']
