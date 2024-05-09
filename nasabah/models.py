from django.db import models


class Nasabah(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    tanggal_lahir = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nama

class Jaminan (models.Model):
    nasabah = models.ForeignKey(Nasabah, related_name="jaminan", on_delete=models.CASCADE)
    barang_jaminan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama