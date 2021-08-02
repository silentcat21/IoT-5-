from accounts.models import User
from django.db import models

# Create your models here.
class Purchase(models.Model):
    customer = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    purchase_goods = models.ForeignKey("product", verbose_name=(""), on_delete=models.CASCADE)
    quantity = models.IntegerField((""))
    delivery_place = models.CharField((""), max_length=50)
