from rest_framework import serializers
from .models import Nasabah, Jaminan

class NasabahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nasabah
        fields = ["nama", "alamat", "nomor_telepon", "saldo", "tanggal_lahir", "email"]

class JaminanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jaminan
        fields = ["nasabah", "barang_jaminan"]