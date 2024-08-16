from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    balance = models.BigIntegerField(verbose_name="موجودی",default=0)