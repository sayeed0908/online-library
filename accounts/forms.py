from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your full name"
        })
    )

    mobile = forms.CharField(
        max_length=20,
        label="Mobile Number",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your mobile number"
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email address"
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Create a password"
        })
    )

    def clean_email(self):

        email = self.cleaned_data["email"].lower()

        if User.objects.filter(username=email).exists():

            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email

    def save(self):

        name = self.cleaned_data["name"]
        mobile = self.cleaned_data["mobile"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        UserProfile.objects.create(
            user=user,
            mobile=mobile
        )

        return user