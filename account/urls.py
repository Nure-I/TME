from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   # path('create_user', views.create_user, name='create_user'),
   # path('directors', views.directors, name='directors'),
   # path('custodians', views.custodians, name='custodians'),
   path('', views.index, name='index'),
   path('register', views.register, name='register'),
   path('login', views.logIn, name='logIn'),
   path('editProfile', views.editProfile, name='profile'),
   path('logOut', views.logOut, name='logOut'),
   # path('log_out', views.log_out, name='log_out'),
   # path('confirm/<int:request_id>/', views.confirm_requests, name='confirm_requests'),
   # path('approve/<int:request_id>/', views.approve_requests, name='approve_requests'),
   path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]