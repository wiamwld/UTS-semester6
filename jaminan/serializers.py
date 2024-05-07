from rest_framework import serializers
from .models import Jaminan

class JaminanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jaminan
        fields = '__all__'
