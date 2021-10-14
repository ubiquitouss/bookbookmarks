from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from . import views

urlpatterns = [
    # post views
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change_frm.html'), name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_dne.html'), name='password_change_done'),
    
    # reset password urls
    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset_frm.html'),
    name='password_reset'),
    path('password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_dne.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_cnfrm.html'),
    name='password_reset_confirm'),
    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name= 'registration/password_reset_cmplt.html'),
    name='password_reset_complete'),
    # path('',include('django.contrib.auth.urls'))

    #user registration
    path('register/', views.register, name='register'),

]