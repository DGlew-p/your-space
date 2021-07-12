from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return HttpResponse("Hello, world. You're at the Seat Selector Home Page.")


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def index(request):
    HttpResponse("this is what authenticated users should see")