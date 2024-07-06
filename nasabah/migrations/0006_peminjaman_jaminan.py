# Generated by Django 5.0.3 on 2024-07-06 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasabah', '0005_peminjaman'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjaman',
            name='jaminan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nasabah.jaminan'),
            preserve_default=False,
        ),
    ]
