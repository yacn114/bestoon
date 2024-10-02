from django.urls import path
from main.views import main,add_transaction
urlpatterns = [
    path('',main,name="main"),
    path('add-transaction/', add_transaction, name='add_transaction'),
    
]
