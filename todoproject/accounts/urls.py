from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name="base"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('signup/', views.CustomSignupView.as_view(), name="signup"),
    path('verify/<token>', views.VerifyView.as_view(), name='verify'),
    path('token/', 
        TemplateView.as_view(template_name = 'token.html'), 
        name="token"
    ),
    path('success/', 
        TemplateView.as_view(template_name = 'success.html'), 
        name="success"
    ),
    path('error/', 
        TemplateView.as_view(template_name = 'error.html'), 
        name='error'
    ),
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
        name='reset_password'
    ),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='token.html'), 
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='new_password.html'), 
        name='password_reset_confirm'
    ),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='success.html'), 
        name='password_reset_complete'
    ),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]