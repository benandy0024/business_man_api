from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.models import Token
from products.models import Expense
User=get_user_model()

class ExpenseSerialiser(serializers.ModelSerializer):
    total=serializers.CharField(read_only=True)
    class Meta:
        model=Expense
        fields=['user','id','title','quantity','price','total']