from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import FAQ

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['user_name', 'question']


from django.contrib.auth.forms import PasswordChangeForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser