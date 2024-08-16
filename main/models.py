from django.db import models

# Create your models here.
class Expensive(models.Model):
    CHOISES = {
        'سیگار':'سیگار',
        'چای':'چای',
        'گیم نت':'گیم نت',
        'خوراکی':'خوراکی',
        'پوشاک':'پوشاک',
        'غذا':'غذا',
    }
    title = models.CharField(choices=CHOISES,max_length=50)
    amount = models.BigIntegerField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self) -> str:
        return self.time + self.title