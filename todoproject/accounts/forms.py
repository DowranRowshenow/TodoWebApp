from tkinter.tix import Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password1", self.error_messages["password_mismatch"])

        return super().clean_password2()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        same_email_user = User.objects.filter(email=email, is_active=True).exists()
        if same_email_user:
            self.add_error("email", ("User with this email already exists!"))

        return email

    def save(self, commit=True): 
        user = super().save(commit=False)
        user.auth_token = str(uuid.uuid4())
        user.is_active = False

        if commit:
            user.save()

        return user