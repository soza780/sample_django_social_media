from django import forms
from django.contrib.auth.models import User


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
            raise forms.ValidationError("password does't match!")
        else:
            return cd["password2"]
