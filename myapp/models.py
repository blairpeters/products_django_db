from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200,unique=True)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'products'


# Run migrations -- creating the tables or updating
#python manage.py makemigrations
#python manage.py migrate