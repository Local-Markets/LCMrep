# Generated by Django 5.0.2 on 2024-03-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_main_page', '0003_alter_products_name_alter_products_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
