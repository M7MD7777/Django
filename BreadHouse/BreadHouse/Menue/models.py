from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    role=models.CharField(max_length=100,default='customer')



class Feedback(models.Model):  
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)  
    text = models.TextField()
    when = models.DateTimeField(default=timezone.now)

class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subcategories'
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,)
    name = models.CharField(max_length=100)  
    description = models.CharField(max_length=100)
    price=models.IntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)


    def __str__(self):
        return self.name


class NewItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class TrendItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE) 

class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.FloatField()

    @property
    def new_price(self):
        discount_decimal = Decimal(str(self.discount / 100))
        discounted_price = self.product.price * (1 - discount_decimal)
        return int(discounted_price)





   

