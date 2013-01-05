from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
 
class Transaction(models.Model):
    key = models.CharField(null = False, blank = False, max_length = 140)
    posted = models.DateTimeField('date Posted')
    description = models.CharField(null = False, blank = True, max_length = 999)
    original_description = models.CharField(null = False, blank = True, max_length = 999)
    amount = models.DecimalField(null = False, max_digits=10, decimal_places=2)
    trans_type = models.CharField(null=False, blank = False, max_length = 20) 
    category = models.CharField(null=False, blank = False, max_length = 50) 
