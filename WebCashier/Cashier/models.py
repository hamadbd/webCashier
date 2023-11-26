from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Manager for CustomUser model, handling user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, password=None):
        # Check if username is provided
        if not username:
            raise ValueError('Users must have a username')

        # Create a new user instance
        user = self.model(
            username=username,
            full_name=full_name,
        )

        # Set password and save user to database
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password):
        # Create a superuser with admin privileges
        user = self.create_user(
            username=username,
            full_name=full_name,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# CustomUser model extending AbstractBaseUser for authentication
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.username

# Product model storing product information
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

# Transaction model recording cashier transactions
class Transaction(models.Model):
    cashier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_items = models.PositiveIntegerField()
    items = models.ManyToManyField(Product, through='TransactionItem')
    transaction_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.pk} by {self.cashier.username}"

# TransactionItem model representing items in a transaction
class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Transaction {self.transaction.pk}"
