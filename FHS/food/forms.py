from django import forms
#from .models import LogIn

# class LogInForm(forms.ModelForm):
#     class Meta:
#         model=LogIn
#         fields="__all__"
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'd-form form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    mobileno = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'd-form form-control'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'mobileno', 'password', 'password1', )
    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

