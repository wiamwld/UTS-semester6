from rest_framework import serializers
from .models import Nasabah, Jaminan, BarangGadai, Pinjaman

class NasabahSerializer(serializers.ModelSerializer):
    jaminan = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Nasabah
        fields = ["id", "nama", "alamat", "nomor_telepon", "tanggal_lahir", "email", "jaminan"]

class JaminanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jaminan
        fields = ["nasabah", "barang_jaminan"]
        
class BarangGadaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangGadai
        fields = ["nama_barang", "deskripsi", "nilai", "tanggal_gadai", "tanggal_jatuh_tempo", "nasabah"]
        
class PinjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pinjaman
        fields = ["pelanggan", "barang", "jumlah_pinjaman", "tanggal_pinjaman", "tanggal_jatuh_tempo", "status"]
