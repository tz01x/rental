from django.urls import path,include,reverse_lazy

from .views import register,account_activation_sent,PasswordResetConfirmViewCoustom,ProfileView
from django.contrib.auth.views import (
     LoginView, LogoutView,
     PasswordResetView,
     PasswordResetDoneView,
     PasswordResetCompleteView,

)
from django.contrib.auth.forms import PasswordResetForm
from .forms import MyLoginForm
app_name='user'
urlpatterns = [

    path('account/profile/', ProfileView.as_view(),name="profile"),
    path('signup/', register,name="signup"),
    path('login/', LoginView.as_view(template_name='login.html',form_class=MyLoginForm), name="login"),
    path('logout/', LogoutView.as_view(template_name='user/logged_out.html'), name="logout"),

    # user email varifications part
    path('profile/account_activation_sent',account_activation_sent.as_view(),name='account_activation_sent'),
    # path('active/account/<uidb64>/<token>/',activate,name='activate'),

    #Forget Password
    path('password-reset/',
        PasswordResetView.as_view(
        template_name='user/password_reset.html',
        subject_template_name='user/password_reset_subject.txt',
        email_template_name='user/password_reset_email.html',
        form_class=PasswordResetForm,
        success_url = reverse_lazy('user:password_reset_done'),
        ),name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmViewCoustom.as_view(),name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name="password_reset_complete"),




]
