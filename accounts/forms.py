from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text="",  # Override help text
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        help_text="",  # Override help text
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(),
        help_text="",  # Override help text
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')
