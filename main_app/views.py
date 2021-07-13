from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import TimeSlot, Profile, Photo
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'silverwareseatselector'

def home(request):
    return render(request, 'home.html')


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
    userList = User.objects.values()
    # displays all usernames including for user currently signed in
    print(userList)
    print(request.user)
    return render(request, 'index.html', {'userList': userList})


def add_photo(request, profile_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, profile_id=profile_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')


class ProfileCreate(CreateView):
  model = Profile
  fields = ['name', 'bio', 'role']
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['name', 'bio', 'role']

class ProfileDelete(DeleteView):
  model = Profile
  success_url = '/'

def profile_detail(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  return render(request, 'profile/detail.html', {'profile': profile })