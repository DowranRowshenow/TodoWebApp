from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from accounts.models import User
from accounts.forms import SingUpForm


class BaseView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('todos'))
        else:
            return render(request, 'base.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    success_url = reverse('todos')


class CustomSignupView(CreateView):
    form_class = SingUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('token')

    def get_success_url(self):
        host = self.request.build_absolute_uri(reverse('verify', args=(self.object.auth_token, )))
        send_verification_mail(self.object, host)

        return super().get_success_url()


def send_verification_mail(user, host):
    subject = 'Your accounts need to be verified'
    message = 'Hi click the link to verify your account ' + host
    sender = settings.EMAIL_HOST_USER
    receiver = [user.email]
    send_mail(subject, message, sender, receiver)


class VerifyView(View):

    def get(self, request, token):
        try:
            user = User.objects.filter(auth_token = token).first()
            if user:
                if user.is_verified:
                    messages.success(request, "Your account is already verified.")
                    return HttpResponseRedirect(reverse('login'))
                else:
                    user.is_active = True
                    user.save()
                    messages.success(request, "Your account has been verified.")
                    return HttpResponseRedirect(reverse('login'))
        except Exception as e:
            print(e)
        return HttpResponseRedirect(reverse('error'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('base'))