from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import User
from accounts.forms import SingUpForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class baseView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/home/page_1')
        else:
            return render(request, 'base.html')


class loginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    success_url = reverse_lazy('main:home')


class signupView(CreateView):
    form_class = SingUpForm
    template_name = 'signup.html'
    success_url = '/token'

    def get_success_url(self):
        send_verification_mail(self.object)

        return super().get_success_url()


def send_verification_mail(user):
    subject = 'Your accounts need to be verified'
    message = 'Hi click the link to verify your account ' + settings.ALLOWED_HOSTS[0] + '/verify/' + user.auth_token
    sender = settings.EMAIL_HOST_USER
    receiver = [user.email]
    send_mail(subject, message, sender, receiver)


class verifyView(View):

    def get(self, request, token):
        try:
            user = User.objects.filter(auth_token = token).first()
            if user:
                if user.is_verified:
                    messages.success(request, "Your account is already verified.")
                    return redirect('/login')
                else:
                    user.is_verified = True
                    user.save()
                    messages.success(request, "Your account has been verified.")
                    return redirect('/login')
        except Exception as e:
            print(e)
        return redirect('/error')


class logoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')