# Generated by Django 5.0.3 on 2024-07-06 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasabah', '0004_remove_nasabah_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_pinjam', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tanggal_pinjam', models.DateTimeField(auto_now_add=True)),
                ('tanggal_jatuh_tempo', models.DateTimeField()),
                ('nasabah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nasabah.nasabah')),
            ],
        ),
    ]
