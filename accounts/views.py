from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        count = 0
        for i in password:
            count += 1

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            return redirect('/accounts/register')

        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('/accounts/register')

        elif count < 8:
            messages.info(request, 'Password Should be contain 8 charecter')
            return redirect('/accounts/register')

        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print("User created!")

            return redirect('/')

    else:
        return render(request, 'register.html')
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'invalid user')
            return redirect('/accounts/login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
