from .serializers import ExpenseSerializer, CategorySerializer, UserSignUpSerializer
from rest_framework import generics, status, response
from .models import Category, Expense
from rest_framework.permissions import IsAuthenticated

# GET and POST a Category
class CategoryListCreate(generics.ListCreateAPIView):

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# GET, DELETE, UPDATE a Category by ID
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


# GET and CREATE an Expense
class ExpenseListCreate(generics.ListCreateAPIView):
   
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#GET, UPDATE and DELETE an Expense by ID
class ExpenseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


# POST a user (Sign Up Authentication Process by Django)
class SignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = []

        

