from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.urls import reverse_lazy, reverse
from accounts.models import User
from accounts.forms import SingUpForm, LogInForm
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(View):

    def get(self, request):
        if request.user.is_authenticated: return HttpResponseRedirect(reverse_lazy('todos'))
        else: return render(request, 'base.html')


class CustomLoginView(LoginView):
    form_class = LogInForm
    template_name = 'login.html'
    success_url = reverse_lazy('todos')
    
    def form_valid(self, form):
        """Handle successful login"""
        response = super().form_valid(form)
        messages.success(self.request, f"Welcome back, {self.request.user.email}!")
        return response
    
    def form_invalid(self, form):
        """Handle login errors"""
        if 'username' in form.errors:
            messages.error(self.request, "Invalid email address or password.")
        elif 'password' in form.errors:
            messages.error(self.request, "Invalid email address or password.")
        else:
            messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class CustomSignupView(CreateView):
    form_class = SingUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('token')

    def form_valid(self, form):
        """Handle successful signup"""
        response = super().form_valid(form)
        # Store email in session for resend functionality
        self.request.session['pending_verification_email'] = self.object.email
        messages.success(self.request, f"Account created successfully! Please check your email ({self.object.email}) to verify your account.")
        link = self.request.build_absolute_uri(reverse('verify', args=(self.object.auth_token, )))
        send_verification_mail(self.object, link)
        return response
    
    def form_invalid(self, form):
        """Handle signup errors"""
        if 'email' in form.errors:
            messages.error(self.request, "This email address is already registered or invalid.")
        elif 'password1' in form.errors:
            messages.error(self.request, "Please ensure your password meets the requirements.")
        elif 'password2' in form.errors:
            messages.error(self.request, "Passwords do not match.")
        else:
            messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    def get_success_url(self):
        return super().get_success_url()


def send_verification_mail(user, link):
    subject = 'Your account needs to be verified'
    sender = settings.EMAIL_HOST_USER
    receiver = [user.email]
    base_url = settings.BASE_DIR.as_posix()  # Or use your site domain if available
    html_content = render_to_string('verification_email.html', {
        'user': user,
        'verification_link': link,
        'base_url': 'https://yourdomain.com',  # Replace with your actual domain
    })
    text_content = f'Hi {user.email},\nPlease verify your account by clicking the following link: {link}'
    email = EmailMultiAlternatives(subject, text_content, sender, receiver)
    email.attach_alternative(html_content, "text/html")
    email.send()


class VerifyView(View):

    def get(self, request, token):
        try:
            user = User.objects.filter(auth_token = token).first()
            if user:
                user.is_active = True
                user.save()
                messages.success(request, "Your account is verified.")
                return HttpResponseRedirect(reverse('login'))
        except Exception as e: print(e)
        return HttpResponseRedirect(reverse('error'))


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You have been successfully logged out.")
        logout(request)
        return HttpResponseRedirect(reverse('base'))


class ResendVerificationEmailView(View):
    def get(self, request):
        email = request.session.get('pending_verification_email')
        if not email:
            messages.error(request, "No pending verification found. Please sign up again.")
            return HttpResponseRedirect(reverse('signup'))
        
        try:
            user = User.objects.get(email=email, is_active=False)
            link = request.build_absolute_uri(reverse('verify', args=(user.auth_token, )))
            send_verification_mail(user, link)
            messages.success(request, f"Verification email has been resent to {email}. Please check your inbox.")
            return HttpResponseRedirect(reverse('token'))
        except User.DoesNotExist:
            messages.error(request, "No unverified account found with this email address.")
            return HttpResponseRedirect(reverse('signup'))
        except Exception as e:
            messages.error(request, "An error occurred while resending the verification email.")
            return HttpResponseRedirect(reverse('signup'))