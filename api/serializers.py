from .models import Category, Expense
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    total_expenses = serializers.ReadOnlyField()
    available_amount = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ['name', 'budget', 'total_expenses', 'available_amount']

class ExpenseSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        slug_field = 'name',
        queryset = Category.objects.all()
    )
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'description', 'date']