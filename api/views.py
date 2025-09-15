from .serializers import ExpenseSerializer, CategorySerializer, UserSignUpSerializer
from rest_framework import generics, status, response
from .models import Category, Expense
from rest_framework.permissions import IsAuthenticated

# GET and POST a Category
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# GET, DELETE, UPDATE a Category by ID
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# GET and CREATE an Expense
class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

#GET, UPDATE and DELETE an Expense by ID
class ExpenseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

# POST a user (Sign Up Authentication Process by Django)
class SignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = []

        

