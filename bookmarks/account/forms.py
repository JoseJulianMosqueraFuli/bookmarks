from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        label="Repeat password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password_confirmation(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password_confirmation"]:
            raise forms.ValidationError("Password do not match")
        return cd["password_confirmation"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["firts_name", "last_name", "email"]


class ProfileEditForm:
    model = Profile
    fields = ["date_of_birth", "photo"]
