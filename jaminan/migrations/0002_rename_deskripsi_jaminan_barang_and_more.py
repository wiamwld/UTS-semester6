# Generated by Django 5.0.3 on 2024-05-06 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jaminan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jaminan',
            old_name='deskripsi',
            new_name='barang',
        ),
        migrations.RenameField(
            model_name='jaminan',
            old_name='nilai',
            new_name='harga',
        ),
    ]
