from rest_framework import serializers
from .models import Nasabah

class NasabahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nasabah
        fields = '__all__'