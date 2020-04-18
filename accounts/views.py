from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django. contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        #Getting the form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password2']

        #Validations
        if password == password_confirmation:

            #Check for duplicated username and email
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register') 
                #Passed the validations
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                #Loggin the user after register
                user.save()
                messages.success(request, 'User registered')
                return redirect('index')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')


    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Loggin out')
        return redirect('index')