
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('profile/<int:profile_id>/', views.profile_detail, name='detail'),
    path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('time/create/', views.TimeSlotCreate.as_view(), name='time_create'),
    path('profile/<int:profile_id>/assoc_timeslot/<int:timeslot_id>/', views.assoc_timeslot, name='assoc_timeslot'),
    


]

