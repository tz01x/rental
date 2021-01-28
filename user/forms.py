

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as gt


from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Citys
# from phonenumber_field.formfields import PhoneNumberField

"""
 Here we are defining four fields namely username, email, password1 and password2; with their own clean_<field_name>() method (except for password1 field).
 Pay close attention to the widget keyword argument in both the password fields. The widget keyword argument allows us to change the default widget of the field.
 Recall that by default, CharField is rendered as text field (i.e <input type="text" ... >).
 To render the CharField as password field we have set widget keyword argument to forms.PasswordInput.

The clean_username() and clean_email() methods check for duplicate username and email respectively.
The clean_password2() method checks whether the password entered in both the fields matches or not. Finally, the save() method saves the data into the database.
"""
# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField( min_length=4, max_length=150, help_text='please file the form with valid info ')
#     email = forms.EmailField(label='Email',help_text='please file the form with valid email id ')
#     password1 = forms.CharField(label="Password",widget=forms.PasswordInput,min_length=6,help_text='Password Should be 6 chareture logo  all numaric chareture not allowed  ')
#     password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput,min_length=6)
#     phone = PhoneNumberField(max_length=16,help_text='Use this forment +88017********* ')
#
#     class Meta:
#         model=User
#         fields=('username','email','phone','password1', 'password2')
#         labels = {
#             'username': _('Unsername'),
#             "phone":_('PhoneNumber'),
#             "password1":_('Password'),
#             "password2":_('Confirm Password'),
#         }
#         help_texts = {
#
#             'phone': _('Use this forment +88017*********'),
#             "password1":_('Password mast be 8 chareture'),
#         }
#     def clean_username(self):
#         username = self.cleaned_data['username'].lower()
#         r = User.objects.filter(username=username)
#         if r.count():
#             raise  ValidationError("Username already exists")
#         return username
#
#     # def clean_email(self):
#     #     email = self.cleaned_data['email'].lower()
#     #     r = User.objects.filter(email=email)
#     #     if r.count():
#     #         raise  ValidationError("Email already exists")
#     #     return email
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Password don't match")
#
#         return password2
# allcitys=[('','-----')]+[(city.name,_(city.name))for city in Citys.objects.all()]

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField( min_length=4, label= _('Username'),max_length=150, help_text=gt('Please fill the form with valid info'))
    email = forms.EmailField(label=_('Email'),help_text='please file the form with valid email id ')
    password1 = forms.CharField(label=_("Password"),widget=forms.PasswordInput,min_length=6,help_text=_('<li>Password mast be 6 chareture long all numaric chareture not allowed</li>'))
    password2 = forms.CharField(label=_("Password confirmation"),widget=forms.PasswordInput,min_length=6)
    # phone = PhoneNumberField(max_length=14,min_length=11,label=_("Phone"),help_text=_('Use this forment +8801*******'))
    phone = forms.CharField(max_length=14,min_length=11,label=_("Mobile number"),help_text=_(''))
    # address=forms.CharField(max_length=200,label=_("Address"),widget=forms.Textarea(attrs={'rows':"2"}))
    city=forms.ChoiceField(choices=[],required=True)
    gender=forms.ChoiceField(choices=[('m',"Male"),('f','Female'),('o',"Other")],required=True)
    class Meta:
        model=User
        fields=('username','email','phone','password1', 'password2','city','gender')
    city.choices=[('','-----')]+[(city.name,_(city.name))for city in Citys.objects.all()]
        # labels = {
        #     'username': _('Unsername'),
        #     "phone":_('PhoneNumber'),
        #     "password1":_('Password'),
        #     "password2":_('Confirm Password'),
        # }
        # help_texts = {
        #
        #     'phone': _('Use this forment +8801777777777'),
        #     "password1":_('Password mast be 8 chareture'),
        # }
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2


class  MyLoginForm(AuthenticationForm):
    username=forms.CharField(max_length=250,label=_('Username or Email'))
    password=forms.CharField(widget=forms.PasswordInput())
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MyLoginForm, self).__init__(*args, **kwargs)


# Notice that CustomUserCreationForm inherits from forms.Form class rather than forms.ModelForm.
