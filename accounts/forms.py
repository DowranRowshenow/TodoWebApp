from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _
from accounts.models import User
import uuid


class SingUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'email',
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        same_email_user = User.objects.filter(email=email, is_active=True).exists()
        if same_email_user:
            self.add_error("email", _("User with this email already exists!"))

        return email

    def save(self, commit=True): 
        user = super().save(commit=False)
        user.auth_token = str(uuid.uuid4())
        user.is_active = False

        if commit:
            user.save()

        return user


class LogInForm(AuthenticationForm):

    def get_invalid_login_error(self):
        self.add_error(
            "username",
            _("Your username or password is incorrect. Please try again!"),
        )

        return super().get_invalid_login_error()

    def confirm_login_allowed(self, user):
        if not user.is_active:
            self.add_error("username", _("Please verify your email!"))

        return super().confirm_login_allowed(user)