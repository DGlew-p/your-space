
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
    


]

