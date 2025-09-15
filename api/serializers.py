from .models import Category, Expense
from rest_framework import serializers
from django.contrib.auth.models import User

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

class UserSignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email','password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
