from user.models import Citys,Messages
from django.shortcuts import render,redirect
from django.urls import reverse

from django.views.generic import TemplateView
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, PasswordChanger

from .sendMail import MailCls
# Create your views here.
# from django.conf import settings
# from django.core.mail import send_mail

# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string

from .tokens import account_activation_token
from main.models import Property
from  .forms import UpdateUserInfo,UpdateProfileInfo
import json 
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name="user/profile.html"
    def get_context_data(self,**kwargs):
        ctx=super(ProfileView,self).get_context_data(**kwargs)
        myproperty=Property.objects.filter(user=self.request.user)
        user_messages=Messages.objects.filter(user=self.request.user)
        ctx['myproperty_list']=myproperty
        ctx['city_list']=Citys.objects.all()
        ctx['user_messages']=user_messages
        # ctx['form_userinfo']=UpdateUserInfo(instance=self.request.user)
        # ctx['form_profileinfo']=UpdateProfileInfo(instance=self.request.user.profile)
        return ctx
    def post(self,*args,**kwargs):
        
        if 'update_profile' in self.request.POST.keys():
            uf=UpdateUserInfo(self.request.POST,instance=self.request.user)
            pf=UpdateProfileInfo(self.request.POST,instance=self.request.user.profile)
            if(uf.is_valid()):
                uf.save()
            else:
                for f in uf:
                    for error in f.errors:
                        messages.add_message(self.request,messages.ERROR,error,"danger")
                # warring messageg
            if(pf.is_valid()):
                pf.save()
            else:
                for f in pf:
                    for error in f.errors: 
                        messages.add_message(self.request,messages.ERROR,error,"danger")
                # messages.error(self.request,"Looks like you inseart wrong credentials")


            if(pf.is_valid() and uf.is_valid()):
                messages.add_message(self.request,messages.SUCCESS,"Profile info update Successfully")
        
        # return render(self.request,self.template_name,self.get_context_data())
        if 'update_password' in self.request.POST.keys():
            pass_form=PasswordChanger(self.request.POST)
            if pass_form.is_valid():
                if(self.request.user.check_password(pass_form.cleaned_data.get('old_password'))) and pass_form.cleaned_data.get('new_password')==pass_form.cleaned_data.get('confirm_password'):
                    self.request.user.set_password(pass_form.cleaned_data.get('confirm_password'))
                    messages.add_message(self.request,messages.SUCCESS,"Your <strong>Password</strong> has been Changed")
            else:
                for field in pass_form:
                    for error in field.errors:
                        messages.add_message(self.request,messages.ERROR,error,"danger")



                    

        return redirect("user:profile")


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

from .forms import  MessageForm

def sendMessagesTo(request):
    if  request.method=="POST":
        form=MessageForm(request.POST)
        # print((request.POST))
        
        modify_msg=request.POST['msg']+"</br> <a href='"+request.POST['property_url']+"'> property link </a> ,"+request.POST['property_url']
        

        # purl=(form.cleaned_data.get('property_url'))
        # print((form.fields['msg'].clean()))
        # print(modify_msg)
        if form.is_valid():
            
            msg_obj=form.save(commit=False)
            msg_obj.msg=modify_msg
            msg_obj.save()
            mail=MailCls()
            mail.run(request=request,to=[msg_obj.user.email,],
            subject=f'[message notification] {msg_obj.name} have some question about you property',
            context={"msg_obj":msg_obj},
            templateName='emailAboutProperty.html'
            )

            return HttpResponse("{\"details\":\"done\",\"status\":200}")
        else:
            error_data={}
            for field in form:
                if field.errors:
                    # print(field.errors)
                    error_data["id_"+field.name]=True
                    # print(form.errors)
            return HttpResponse(content='{"status":400,"details":'+json.dumps(error_data)+'}')
        
        
    return HttpResponseBadRequest

