from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="enter password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="enter password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def cleaned_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd["password2"]:
            raise forms.ValidationError("password doesn't match!")
        else:
            return cd["password2"]

    def clean_email(self):
        data = self.cleaned_data['email'].lower()
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already registered!")
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id) \
                         .filter(email=data)
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data
