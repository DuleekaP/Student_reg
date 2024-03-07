# forms.py
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size': '40'}))


class BioDataForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ariyasinghe Hamuge Saman Kumara Ratnayake'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}))
    nic = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '9999999999V'}))
    gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')))
    marital_status = forms.ChoiceField(choices=(('Single', 'Single'), ('Married', 'Married')))

class EmergencyContactFrom(forms.Form):
    E_name = forms.CharField(max_length=100)
    E_relationship = forms.CharField(max_length=50)
    E_address = forms.CharField(max_length=100)
    E_contact = forms.CharField(max_length=12)
