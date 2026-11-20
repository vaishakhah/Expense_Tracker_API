from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=50)
    amount = models.IntegerField()
    category_choices = (('food','Food'),
                    ('bill','Bill'),
                    ('entertainment','Entertainment'),
                    ('shopping','Shopping'),
                    ('others','Others'))
    category = models.CharField(max_length=40,choices=category_choices)
    priority_choices = (('need','Need'),
                        ('want','Want'))
    priority = models.CharField(max_length=40,choices=priority_choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_choices = (('upi','Upi'),
                       ('cash','Cash'))
    payment = models.CharField(max_length=40,choices=payment_choices)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
