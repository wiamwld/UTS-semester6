from django.db import models

class Nasabah(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    tanggal_lahir = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nama

class Jaminan (models.Model):
    nasabah = models.ForeignKey(Nasabah, related_name="jaminan", on_delete=models.CASCADE)
    barang_jaminan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class BarangGadai(models.Model):
    nama_barang = models.CharField(max_length=100)
    deskripsi = models.TextField()
    nilai = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_gadai = models.DateField(auto_now_add=True)
    tanggal_jatuh_tempo = models.DateField()
    nasabah = models.ForeignKey(Nasabah, related_name="BarangGadai", on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_barang
    
class Pinjaman(models.Model):
    pelanggan = models.ForeignKey(Nasabah, on_delete=models.CASCADE)
    barang = models.ForeignKey(Jaminan, on_delete=models.CASCADE)
    jumlah_pinjaman = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_pinjaman = models.DateField(auto_now_add=True)
    tanggal_jatuh_tempo = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('selesai', 'Selesai')], default='pending')

    def __str__(self):
        return f"Pinjaman {self.pelanggan.nama_lengkap} - {self.barang.nama_barang}" 