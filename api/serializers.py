from rest_framework import serializers
from api.models import ME

class MESerializer(serializers.ModelSerializer):
    class Meta:
        model = ME
        fields = '__all__'