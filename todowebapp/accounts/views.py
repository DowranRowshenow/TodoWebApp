import uuid
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Profile

class baseView(TemplateView):
    template_name = 'base.html'

class successView(TemplateView):
    template_name = 'success.html'

class errorView(TemplateView):
    template_name = 'error.html'

class tokenView(TemplateView):
    template_name = 'token.html'

class loginView(TemplateView):
    def post(self, request):
        email = request.POST['email']
        username = str(email).replace("@gmail.com", "")
        password = request.POST['password']
        user_obj = User.objects.filter(email = email).first()
        if (user_obj is None):
            messages.success(request, "User not found")
            return redirect('/login')
        profile_obj = Profile.objects.filter(user = user_obj).first()
        if (not profile_obj.is_verified):
            messages.success(request, "User is not verified please check your mail")
            return redirect('/login')
        user = authenticate(username = username, password = password)
        if (user is None):
            messages.success(request, "Wrong password.")
            return redirect('/login')
        login(request, user)
        return redirect('/home')
    template_name = 'login.html'

class signupView(TemplateView):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        username = str(email).replace("@gmail.com", "")
        try:
            if (User.objects.filter(email = email).first()):
                messages.success(request, "Email is taken.")
                return redirect('/signup')
            if (len(password) < 8):
                messages.success(request, "Password is too short.")
                return redirect('/signup')
            if (len(password) > 50):
                messages.success(request, "Password is too long.")
                return redirect('/signup')
            if (" " in password):
                messages.success(request, "Password cannot contain spaces.")
                return redirect('/signup')
            if (not password == password_2):
                messages.success(request, "Password entries are not the same.")
                return redirect('/signup')
            user_obj = User.objects.create(username = username, email = email)
            user_obj.set_password(password)
            auth_token = str(uuid.uuid4())
            profile_obj = Profile(user = user_obj, auth_token = auth_token)
            send_email_for_verification(email, auth_token)
            user_obj.save()
            profile_obj.save()
            return redirect('/token')
        except Exception as e:
            print(e)
            return redirect('/signup')
    template_name = 'signup.html'

def send_email_for_verification(email, token):
    subject = "Your accounts need to be verified"
    message = 'Hi click the link to verify your account ' + '127.0.0.1:8000' + '/verify/' + token
    email_from = settings.EMAIL_HOST_USER
    receiver = [email]
    send_mail(subject, message, email_from, receiver)

class verifyView(View):
    def get(self, request, token):
        try:
            profile_obj = Profile.objects.filter(auth_token = token).first()
            if (profile_obj):
                if (profile_obj.is_verified):
                    messages.success(request, "Your account is already verified.")
                    return redirect('/login')
                else:
                    profile_obj.is_verified = True
                    profile_obj.save()
                    messages.success(request, "Your account has been verified.")
                    return redirect('/login')
        except Exception as e:
            print(e)
        return redirect('/error')

class forgotPasswordView(View):
    def get(self, request, email):
        try:
            user = User.objects.filter(email=email).first()
            profile = Profile.objects.filter(user = user).first()
            send_email_for_forgot_password(email, profile.auth_token)
            messages.success(request, "Password reset email is sent. Please check your email.")
            return redirect('/login')
        except Exception as e:
            print(e)
        return redirect('/login')

def send_email_for_forgot_password(email, token):
    subject = "Password Reset Request"
    message = 'Hello, please click to the link to creeate new password ' + '127.0.0.1:8000' + '/password_reset/' + token
    email_from = settings.EMAIL_HOST_USER
    receiver = [email]
    send_mail(subject, message, email_from, receiver)

class passwordResetView(View):
    def get(self, request, token):
        try:
            profile_obj = Profile.objects.filter(auth_token = token).first()
            if (profile_obj):
                return render(request, 'password_reset.html')
        except Exception as e:
            print(e)
            return redirect('/error')
    def post(self, request, token):
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        pageUrl = "/password_reset/" + token
        try:
            if (len(password) < 8):
                messages.success(request, "Password is too short.")
                return redirect(pageUrl)
            if (len(password) > 50):
                messages.success(request, "Password is too long.")
                return redirect(pageUrl)
            if (" " in password):
                messages.success(request, "Password cannot contain spaces.")
                return redirect(pageUrl)
            if (not password == password_2):
                messages.success(request, "Password entries are not the same.")
                return redirect(pageUrl)
            profile_obj = Profile.objects.filter(auth_token = token).first()
            user_obj = profile_obj.user
            user_obj.set_password(password)
            new_token = str(uuid.uuid4())
            profile_obj.auth_token = new_token
            user_obj.save()
            profile_obj.save()
            messages.success(request, "New password created successfully.")
            return redirect('/login')
        except Exception as e:
            print(e)
            return redirect(pageUrl)

class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')