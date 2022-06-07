import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_with, logout as logout_with
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Profile

def base(request):
    return render(request, 'base.html')

def login(request):
    if (request.method == "POST"):
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
        login_with(request, user)
        return redirect('/home')
    return render(request, 'login.html')

def signup(request):
    if (request.method == "POST"):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        username = str(email).replace("@gmail.com", "")
        try:
            if (User.objects.filter(email = email).first()):
                messages.success(request, "Email is taken.")
                return redirect('/signup')
            if (User.objects.filter(username = username).first()):
                messages.success(request, "Username is taken.")
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
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile(user = user_obj, auth_token = auth_token)
            profile_obj.save()
            send_mail_for(email, auth_token)
            return redirect('/token')
        except Exception as e:
            print(e)
    return render(request, 'signup.html')

def token(request):
    return render(request, 'token.html')

def send_mail_for(email, token):
    subject = "Your accounts need to be verified"
    message = 'Hi click the link to verify your account http://127.0.0.1:8000/verify/' + token
    email_from = settings.EMAIL_HOST_USER
    receiver = [email]
    send_mail(subject, message, email_from, receiver)

def verify(request, token):
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
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def error(request):
    return render(request, 'error.html')

def success(request):
    return render(request, 'success.html')

def forgot_password(request, email):
    user = Profile.objects.filter(email=email).first()
    send_mail_for(email, user.auth_token)
    return redirect('/login')

def logout(request):
    logout_with(request)
    return redirect('/')