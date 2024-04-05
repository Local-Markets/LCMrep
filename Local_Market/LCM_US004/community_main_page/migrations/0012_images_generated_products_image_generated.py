# Generated by Django 5.0.2 on 2024-04-05 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_main_page', '0011_alter_products_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='images_generated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ia_image', models.ImageField(null=True, upload_to='ia_images/')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='image_generated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community_main_page.images_generated'),
        ),
    ]
