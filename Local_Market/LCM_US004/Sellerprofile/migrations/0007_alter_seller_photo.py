# Generated by Django 5.0.2 on 2024-04-14 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sellerprofile', '0006_alter_seller_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
