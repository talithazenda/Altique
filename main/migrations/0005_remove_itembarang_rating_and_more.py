# Generated by Django 5.1.1 on 2024-11-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_itembarang_category_itembarang_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itembarang',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='itembarang',
            name='waktu_buat',
        ),
    ]