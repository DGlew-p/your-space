
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_request, name ="login"),
    path('index/', views.index, name='index'),

    path("user/<int:user_id>/", views.userpage, name = "userpage"),
    path('user/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('user/<int:user_id>/update/', views.profile_update, name='profile_update'),

    path('user/<int:user_id>/assoc_timeslot/<int:timeslot_id>/', views.assoc_timeslot, name='assoc_timeslot'),
    path('user/<int:user_id>/unassoc_timeslot/<int:timeslot_id>/', views.unassoc_timeslot, name='unassoc_timeslot'),
    path('user/<int:user_id>/timeslot/', views.timeslot_index, name='timeslot_index'),

    path('user/<int:user_id>/add_photo/',views.add_photo, name='add_photo'),
    path('user/<int:user_id>/delete_photo/',views.photo_delete, name='delete_photo'),

]
