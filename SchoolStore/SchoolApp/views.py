from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import CustomUser


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('info')
        else:
            messages.info(request, 'Invalid login credentials')

            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successfull')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def info(request):
    messages.success(request, 'Registration successfull')

    return render(request, 'registertion.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
