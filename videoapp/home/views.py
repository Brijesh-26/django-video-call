from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def handleRegister(request):
    if request.method=="POST":
        print('welcome to post method')
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            print('password is not mathcing')
            return render(request,'register.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                print('email is already taken')
                messages.info(request,"Email is Taken")
                return render(request,'register.html')
        except Exception as identifier:
            pass
        print('new user creating')
        user = User.objects.create_user(email,email,password)
        
        user.save()
        user.is_active=True
        print('user craeted and saved to db')
        return redirect('/login/')
    print('executing get mehtod')
    return render(request,"register.html")

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pass1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or the homepage
            return redirect('/home/')
        else:
            # Display an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('/login/')

    # If the request method is GET, display the login form
    return render(request, 'login.html')

def handleLogOut(request):
    logout(request)
    return redirect('/login/')

def handleHome(request):
    return render(request, 'home.html')


def videocall(request):
    return render(request, 'videochat.html')

def join(request):
    return render(request, 'joinmeeting.html')
