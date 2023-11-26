"""WebCashier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cashier/', include('Cashier.urls')),

    # JWT token authentication URLs , These endpoints are responsible for token generation, refreshing, and verification, which are used for user authentication

    #This endpoint is used to obtain an access token by providing valid credentials (username and password) via a POST request.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain token
    # This endpoint is used to refresh an access token by providing a valid refresh token via a POST request.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    #This endpoint is used to verify the validity of an access token by providing it via a POST request.
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify token
]
