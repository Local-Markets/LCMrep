from django.db import models
from django.contrib.auth.models import User as django_model_user

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length = 40)
    price = models.CharField(max_length = 15)
    description = models.TextField(max_length = 250)
    image = models.ImageField(upload_to="images/", null=True)
    rating = models.IntegerField(null = True, default = 0)
  
class ProductUser(models.Model):
    user_info = models.ForeignKey(django_model_user, on_delete = models.CASCADE, default = 1)
    product_info = models.ForeignKey(products, on_delete=models.CASCADE, default = 1)
    
