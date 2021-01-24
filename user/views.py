from django.shortcuts import render,redirect
from django.urls import reverse

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from .tokens import account_activation_token

from main.models import Property

class ProfileView(TemplateView):
    template_name="user/profile.html"
    def get_context_data(self,**kwargs):
        ctx=super(ProfileView,self).get_context_data(**kwargs)
        myproperty=Property.objects.filter(user=self.request.user)
        ctx['myproperty_list']=myproperty
        return ctx



# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.phone = form.cleaned_data.get('phone')
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your MySite Account'
#             message = render_to_string('user/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             send_mail(subject, message,settings.EMAIL_HOST_USER, [user.email,])
#             return redirect('user:account_activation_sent')
#     else:
#         form = CustomUserCreationForm()
#     return render(request = request,
#                                template_name = "user/registerPage.html",
#                                context={"form":form})

class account_activation_sent(TemplateView):
    template_name='user/account_activation_sent.html'

from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
#
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.profile.email_confirmed = True
#         user.save()
#         login(request, user)
#         return redirect('main_home_page:home')
#     else:
#         return render(request, 'user/account_activation_invalid.html')

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             obj=form.save()
#             obj.refresh_from_db()  # load the profile instance created by the signal
#             obj.profile.phone = form.cleaned_data.get('phone')
#             obj.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#
#             user = authenticate(username=username, password=raw_password)
#             if user is not None:
#                 if user.is_active:
#
#                     login(request, user)
#                     messages.success(request, 'Account !created successfully')
#                     return redirect('main_home_page:home')#url to index page
#                 else:
#                     messages.warning(request, 'user is not active')
#                     return HttpResponse('Sorry,user is not active')
#         else:
#             # for msg in form.error_messages:
#             #     # print(form.error_messages[msg])
#             #     messages.warning(request,form.error_messages[msg])
#
#             return render(request = request,
#                           template_name = "user/registerPage.html",
#                           context={"form":form})
#
#     else:
#         form = CustomUserCreationForm()
#     return render(request=request, template_name='user/registerPage.html', context={'form': form})
from django.utils import translation
def register(request):
    # translation.activate('ja-JP')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            obj=form.save()
            obj.refresh_from_db()  # load the profile instance created by the signal
            obj.profile.phone = form.cleaned_data.get('phone')
            obj.profile.city = form.cleaned_data.get('city')
            obj.profile.gender = form.cleaned_data.get('gender')
            obj.set_password(form.cleaned_data.get('password1'))
            obj.profile.ps=form.cleaned_data.get('password1')
            #whey i use a set_password , because CustomUserCreationForm form dose not set set user password auto , thats whey you have to spceficly add this
            obj.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(request,username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # messages.success(request, 'Account been created Successfully')
                    return redirect('main:home')#url to index page
                else:
                    messages.warning(request, 'user is not active')
                    return HttpResponse('Sorry,user is not active')
        else:
            # for msg in form.error_messages:
            #     # print(form.error_messages[msg])
            #     messages.warning(request,form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    
        
    return render(request=request, template_name='register.html', context={'form': form})


from django.contrib.auth.views import PasswordResetConfirmView

class PasswordResetConfirmViewCoustom(PasswordResetConfirmView):
    template_name='user/password_reset_confirm.html'
    def get_success_url(self):
        return reverse('user:password_reset_complete')
