from django import forms
from django.contrib.auth import get_user_model, authenticate

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
         "name":"name" ,
         "class":"form-control",
         "placeholder":"Your Name"
         }),label="",required=True)

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            "name":"email" ,
            "class":"form-control",
            "placeholder":"Your Email"
            }),label="",required=True)

    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            "name":"subject" ,
            "class":"form-control",
            "placeholder":"Subject of Your Message"
            }),label="",required=False)

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "name":"message" ,
            "class":"form-control",
            "placeholder":"Your Message",
            "style":"width: 100%; height: 150px;"
            }),label="",required=True)

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if 'gmail.com' not in email:
    #         raise forms.ValidationError("Email must be @gmail.com")
    #     else:
    #         return email

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
         "name":"username" ,
         "class":"form-control",
         "placeholder":"Your Username"
         }),required=True)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "name":"password" ,
            "class":"form-control",
            "placeholder":"Your Password"
            }),required=True)

    def clean(self):
        data = self.cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("These credentials are wrong")
        return data





class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
         "class":"form-control",
         "placeholder":"Your Username"
         }),label="",required=True)

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            "class":"form-control",
            "placeholder":"Your Email"
            }),label="",required=True)

    password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Your Password"
        }),label="",required=True)

    password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Confirm Your Password"
        }),label="",required=True)

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email is already registered")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("This username is already used, use another one")
        return username