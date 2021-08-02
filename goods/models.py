from accounts.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField((""), max_length=50)
    regist_date = models.DateField((""), auto_now=True, auto_now_add=False)
    product_review = models.ForeignKey("review", verbose_name=(""), on_delete=models.CASCADE)
    description = models.CharField((""), max_length=50)
    product_content = models.TextField((""))
    stock = models.IntegerField((""))


    

class Review(models.Model):
    goods = models.ForeignKey("product", verbose_name=(""), on_delete=models.CASCADE)
    writer = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    review_content = models.TextField((""))