from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Categories Model

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=9, decimal_places=2)
    

    @property
    def total_expenses(self):
        total_amount = 0
        for row in self.expense_set.all():
            total_amount += row.amount
        return total_amount
    
    @property
    def available_amount(self):
        return self.budget - self.total_expenses
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount}"