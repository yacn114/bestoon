from django.contrib import admin
from main.models import Expensive,Income,Title_Expensive,Title_Income
# Register your models here.
admin.site.register(Expensive)
admin.site.register(Income)
admin.site.register(Title_Income)
admin.site.register(Title_Expensive)
