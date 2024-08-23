from django.db import models
from user.models import User
# Create your models here.
class Title_Expensive(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Expensive(models.Model):
    title = models.ManyToManyField(Title_Expensive)
    amount = models.BigIntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.date.month}/{self.date.day} : {self.amount:,} : {self.title}"

class Title_Income(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Income(models.Model):
    title = models.ManyToManyField(Title_Income)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return f"{self.date.month}/{self.date.day} : {self.amount:,} "


#TODO; add signal for all amount
#TODO; add bot telegram {telebot}
#TODO; add drf