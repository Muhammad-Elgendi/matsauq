from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, get_user_model, logout

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context ={
        "title":"Matsauq | An AI based ecommerce store"
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    context ={
        "title":"Contact Us | Matsauq",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)

    return render(request,"contact/view.html",context)

def logout_page(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm(request.POST or None)
    context = {
        "title":"Login | Matsauq",
        "form": form
    }    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            print(form.cleaned_data)
            return redirect("/")

    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = RegisterForm(request.POST or None)
    context = {
        "title":"Register | Matsauq",
        "form": form
    }    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)    

        # login that user
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            print("Logging in",form.cleaned_data)
            return redirect("/")
        
    return render(request,"auth/register.html",context)

def about_page(request):
    return HttpResponse("about_page page")
