from django.urls import path
from .views import (
    CustomUserListCreateView,
    CustomUserDetailView,
    ProductListCreateView,
    ProductDetailView,
    TransactionListCreateView,
    TransactionDetailView,
)

urlpatterns = [
    # URLs for CustomUser model
    path('users/', CustomUserListCreateView.as_view(), name='user-list'),  # List and create CustomUser
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),  # Detail view for CustomUser

    # URLs for Product model
    path('products/', ProductListCreateView.as_view(), name='product-list'),  # List and create Product
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # Detail view for Product

    # URLs for Transaction model
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),  # List and create Transaction
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    # Detail view for Transaction
]
