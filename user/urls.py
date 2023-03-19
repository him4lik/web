from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('otp/', views.OTPView.as_view(), name='otp-page'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]