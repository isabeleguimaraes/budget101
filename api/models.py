from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

# Categories Model

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        unique_together = ['user', 'name']
    

    @property
    def total_expenses(self):
        return self.expense_set.aggregate(Sum('amount'))['amount__sum'] or 0
    
    @property
    def available_amount(self):
        return self.budget - self.total_expenses
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount}"