from rest_framework import serializers
from .models import Nasabah, Jaminan, BarangGadai

class NasabahSerializer(serializers.ModelSerializer):
    jaminan = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Nasabah
        fields = ["nama", "alamat", "nomor_telepon", "saldo", "tanggal_lahir", "email", "jaminan"]

class JaminanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jaminan
        fields = ["nasabah", "barang_jaminan"]
        
class BarangGadaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangGadai
        fields = ["nama_barang", "deskripsi", "nilai", "tanggal_gadai", "tanggal_jatuh_tempo", "nasabah"]