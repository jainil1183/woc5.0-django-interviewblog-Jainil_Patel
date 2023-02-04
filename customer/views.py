from django.shortcuts import render,redirect
from django.contrib import messages
#from .forms import customerForm
#from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import customer

def login(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/home/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")
    else:
        return render(request, 'login.html/')

def index(request):
    if request.user.is_authenticated:
        return redirect("home/")
    return render(request,'index.html/')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        degree = request.POST['degree']
        program = request.POST['program']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        graduation_year = request.POST['graduation_year']

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = first_name
        myuser.last_name = last_name

        if password2 != password1:
            messages.error(request, " Passwords do not match")
            return redirect('register')

        myuser.save()
        customer_details = customer(username=myuser, degree=degree, program=program, graduation_year=graduation_year)
        customer_details.save()
        messages.success(request,"Successfully Created")
        return redirect('index')

    else:
        return render(request, 'register.html/')

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('index')
    else:
        return render(request, 'ano_user.html/')

# Create your views here.
