from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, ExpenseListCreate, ExpenseRetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(),name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('expenses/', ExpenseListCreate.as_view(), name= 'expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroy.as_view(), name='expense-detail')
]