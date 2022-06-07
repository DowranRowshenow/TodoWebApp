from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('token/', views.token, name="token"),
    path('verify/<token>', views.verify, name='verify'),
    path('success/', views.success, name="success"),
    path('error/', views.error, name='error'),
    path('forgot_password/<email>', views.forgot_password, name="forgot_password"),
    path('logout/', views.logout, name="logout"),
]
