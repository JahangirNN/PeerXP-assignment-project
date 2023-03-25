from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority


class Expense(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    priority = models.CharField(max_length=2 , choices=priority_choices)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date_of_expense = models.DateTimeField(auto_now_add=True, editable=True)  
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    description = models.TextField(max_length=300)
    ammount = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        super(Expense, self).save(*args, **kwargs)