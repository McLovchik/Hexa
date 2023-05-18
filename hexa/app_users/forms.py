# import uuid
# from datetime import timedelta

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
# from django.utils.timezone import now

from .models import EmailVerification, User

from .tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your username."
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter your password."
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name.'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name.'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username.'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email.'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password.'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-enter your password.'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        # expiration = now() + timedelta(hours=48)
        # record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        # record.send_verification_email()
        # return user

        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name.'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name.'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username.', 'readonly': True
    }))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={

    }), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your email.', 'readonly': True
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'username', 'email')

