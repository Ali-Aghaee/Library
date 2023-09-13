from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']
        help_texts= {
            'username':None,
        }
        extra_kwargs = {"password":{'write_only': True}}
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget= forms.PasswordInput())
    
class UserInfoForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts= {
            'username':None,
        }