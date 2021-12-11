from django.contrib import admin
from .models import Category, TransactionType, Transactions

# Register your models here.
admin.site.register(Category)
admin.site.register(TransactionType)
admin.site.register(Transactions)
