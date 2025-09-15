from os import name
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, ExpenseListCreate, ExpenseRetrieveUpdateDestroy, SignUpView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(),name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('expenses/', ExpenseListCreate.as_view(), name= 'expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroy.as_view(), name='expense-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('signup/', SignUpView.as_view(), name='sign-up')
]