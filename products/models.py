from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
User = settings.AUTH_USER_MODEL


class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def update_total(self):
        item_price = self.price
        item_quantity = self.quantity
        new_total = item_price * item_quantity
        self.total = new_total
        self.save()
        return new_total

class Sale(models.Model):
    title=models.CharField(max_length=120,blank=False)
    category=models.CharField(max_length=120)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)






def post_item_total(sender, instance=None, created=False, **kwargs):
    if created:
        instance.update_total()


post_save.connect(post_item_total, sender=Expense)
