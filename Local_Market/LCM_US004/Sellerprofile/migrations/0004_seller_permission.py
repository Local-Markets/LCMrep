# Generated by Django 5.0.2 on 2024-04-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sellerprofile', '0003_seller_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='permission',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
