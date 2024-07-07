# Generated by Django 5.0.3 on 2024-07-07 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nasabah', '0008_rename_jumlah_pinjam_peminjaman_nilai_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peminjaman',
            old_name='nilai',
            new_name='jumlah_pinjam',
        ),
        migrations.RenameField(
            model_name='peminjaman',
            old_name='tanggal_gadai',
            new_name='tanggal_pinjam',
        ),
        migrations.RemoveField(
            model_name='peminjaman',
            name='deskripsi',
        ),
        migrations.RemoveField(
            model_name='peminjaman',
            name='nama_barang',
        ),
    ]
