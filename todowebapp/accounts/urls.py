from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.baseView.as_view(), name="base"),
    path('login/', views.loginView.as_view(), name="login"),
    path('signup/', views.signupView.as_view(), name="signup"),
    path('token/', views.tokenView.as_view(), name="token"),
    path('verify/<token>', views.verifyView.as_view(), name='verify'),
    path('success/', views.successView.as_view(), name="success"),
    path('error/', views.errorView.as_view(), name='error'),
    path('forgot_password/<email>', views.forgotPasswordView.as_view(), name="forgot_password"),
    path('password_reset/<token>', views.passwordResetView.as_view(), name="password_reset"),
    path('logout/', views.logoutView.as_view(), name="logout"),
]
