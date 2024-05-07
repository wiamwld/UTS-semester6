from django.db import models
from nasabah.models import Nasabah

class Jaminan(models.Model):
    nama = models.ForeignKey(Nasabah, on_delete=models.CASCADE)
    barang = models.TextField()
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    tanggal_pembaruan = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama
