# Generated by Django 4.2.7 on 2024-05-02 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sellerprofile', '0009_seller_active_seller'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community_main_page', '0004_products_seller_info_alter_productuser_product_info'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='productuser',
            name='user_info',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
