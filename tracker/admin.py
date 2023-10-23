from django.contrib import admin
from .models import Expense, Income

# Register the Expense and Income models
admin.site.register(Expense)
admin.site.register(Income)