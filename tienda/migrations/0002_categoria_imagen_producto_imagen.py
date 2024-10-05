# Generated by Django 5.1 on 2024-09-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='categorias/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
