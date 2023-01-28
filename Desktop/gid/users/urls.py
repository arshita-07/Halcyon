
from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_main',user_views.login_main, name = "login_main"),
    path('signup_main',user_views.signup_main, name = "signup_main"),
    path('user_signup/', user_views.register, name="user_signup"),
    path('user_login/', auth_views.LoginView.as_view(template_name='Login.html'), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='Logout.html'), name="logout"),
    path('Client_profile/', user_views.update_profile_Client, name="Client_profile"),
    path('admin_profile/', user_views.update_profile_admin, name="admin_profile"),
    path('Hospital_profile/', user_views.update_profile_Hospital, name="Hospital_profile"),
    path('Hospital_login/', user_views.Hospital_login, name="Hospital_login"),
    path('Hospital_signup/', user_views.Hospital_register, name="Hospital_signup"),
    path('admin_login/', user_views.admin_login, name="admin_login"),
    path('admin_signup/', user_views.admin_register, name="admin_signup"),
    path("eh/",user_views.eh_view,name='eh'),
    path("Hospital_request/",user_views.Hospital_request_view,name='Hospital_request'),
    path('change_status/<int:pk>/',user_views.change_status, name='change_status'),
    path('verification_pending/',user_views.verification_wait_view, name = 'verification_wait'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
]