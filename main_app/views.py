from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login


def home(request):
    return HttpResponse("login or signup")

def signup(request):
    return HttpResponse("sign up")

def index(request):
    return HttpResponse("What user sees once they sign in successfully")

