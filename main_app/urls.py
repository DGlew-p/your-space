
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_request, name ="login"),
    path("user/<int:user_id>/", views.userpage, name = "userpage"),
    path('user/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('user/<int:user_id>/update/', views.profile_update, name='profile_update'),
    path('user/<int:user_id>/assoc_timeslot/<int:timeslot_id>/', views.assoc_timeslot, name='assoc_timeslot'),
    path('index/', views.index, name='index'),
    path('user/<int:user_id>/assoc_timeslot/<int:timeslot_id>/', views.assoc_timeslot, name='assoc_timeslot'),
    path('user/<int:user_id>/unassoc_timeslot/<int:timeslot_id>/', views.unassoc_timeslot, name='unassoc_timeslot'),

#     path('profile/<int:profile_id>/', views.profile_detail, name='detail'),
    path('user/<int:profile_id>/add_photo/',views.add_photo, name='add_photo'),
#     path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),

#     path('profile/<int:pk>/delete/',
#          views.ProfileDelete.as_view(), name='profile_delete'),
#     path('timeslot/<int:pk>/', views.TimeslotDetail.as_view(),
#          name='timeslot_detail'),


]
