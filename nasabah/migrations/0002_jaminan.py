# Generated by Django 5.0.3 on 2024-05-09 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasabah', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jaminan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barang_jaminan', models.CharField(max_length=200)),
                ('nasabah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jaminan', to='nasabah.nasabah')),
            ],
        ),
    ]
