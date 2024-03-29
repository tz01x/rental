from django import  forms
from django.db import models
from django.forms import fields
from django.utils.translation import gettext_lazy as _
from .models import Property,PropertyType,FeatureType,Utilities,Preference,Contact
from django.contrib.auth import get_user_model
from user.models import Citys

class FeatureForm(forms.ModelForm):
    ptype=forms.ModelMultipleChoiceField(
    queryset=PropertyType.objects.all(),
    widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model=FeatureType
        fields='__all__'


# allcitys=lambda : [('','----')]+[(city.name,_(city.name))for city in Citys.objects.all()]
class PropertyForm(forms.ModelForm):
    user=forms.ModelChoiceField(widget=forms.HiddenInput,queryset=get_user_model().objects.all(),disabled=True)
    description=forms.CharField(widget=forms.Textarea(attrs={"rows":"2"}))

    # advance_payment=forms.DecimalField(min_value=0)
    price=forms.DecimalField(min_value=0,label="Rent Price per month")
    available_from=forms.DateField(widget=forms.DateInput(attrs={'autocomplete':"off"}))
    city=forms.ChoiceField()
    area=forms.CharField()
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':'2'}))

    # if the field is disable then you django wont be retrive thos data if you put the value of the form field manually , 
    lat=forms.CharField(required=False,widget=forms.HiddenInput)
    lng=forms.CharField(required=False,widget=forms.HiddenInput)


    mymap=forms.CharField(required=False,label="Set Your Property Location")
    class Meta:
        model=Property
        fields=['user',
                'property_types',
                'title',
                'description',
                'available_from',
                'city',
                'lat',
                'lng',
                'mymap',
                'area',
                # 'thana',
                'address',
                'contact_person',
                # 'advance_payment',
                'price',
                'publish'
                ]

    available_from.widget.attrs.update({"id":"datepicker"})
    city.widget.attrs.update({'id':'selected_city'})
    # city.choices=[('','----')]+[(city.name,_(city.name))for city in Citys.objects.all()]
    area.widget.attrs.update({'id':'selected_area'})
    def __init__(self,*args,**kwargs):

        super(PropertyForm, self).__init__(*args,**kwargs)
        
        self.fields['city'].choices=[('','----')]+[(city.name,_(city.name))for city in Citys.objects.all()]



    # def clean_area(self):
    #     super(PropertyForm,self).clean_area()
    #     print("here")
    #     area_name = self.cleaned_data['area']
    #     if len(area_name)==0:
    #         raise ValueError('Please select your designated area!')
    #     try:
    #         obj=Districts.objects.get(name=area_name)
    #         if obj:
    #             return area_name
    #     except :
    #         raise  ValueError('Please select an Valid area!')
    # def clean(self):
        # clean_data=super(PropertyForm,self).clean()
        # print('here')
        # print(clean_data)
        # value=self.cleaned_data.get('area',None)

        # self.area._set_choices((value,value))




Set_Available_choices=[(str(i),f'{i} set') for i in range(1,10)]
class PropertyFormPart2(forms.ModelForm):
    feature_types=forms.ModelMultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple(),
    queryset=FeatureType.objects.all(),
    )
    utility_bill=forms.ModelMultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    queryset=Utilities.objects.all(),
    )
    # preference=forms.ModelMultipleChoiceField(
    # required=False,
    # widget=forms.CheckboxSelectMultiple,
    # queryset=Preference.objects.all(),
    # )
    set_available=forms.ChoiceField(choices=Set_Available_choices,required=False)
    parking_space=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)
    youtube_link=forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}),required=False)

    class  Meta:
        model=Property
        fields=[
            'property_size',
            # 'ad_for',
            # 'hostal_type',
            'roommate_type',
            'people_per_room',
            'set_available',

            'bedroom',
            'living_room',
            'bathroom',
            'drawing_room',
            'kitchen',
            'balcony',
            'youtube_link',
            'parking_space',
            'feature_types',
            'utility_bill',
            # 'preference'
            ]
        # exclude=['id']
        # widgets ={
        # 'set_available':forms.HiddenInput(),
        # }
    feature_types.widget.attrs.update({'class':'form-check-input'})
    utility_bill.widget.attrs.update({'class':'form-check-input'})
    # preference.widget.attrs.update({'class':'form-check-input'})



    def __init__(self,*args,**kwargs):
        # pop the property_type_id
        ptypeId=kwargs.pop('property_type_id',None)
        super(PropertyFormPart2,self).__init__(*args, **kwargs)

        if ptypeId is not None:

            ptype_obj=PropertyType.objects.get(id=ptypeId)
            #usign back relation with the help of related_name get all the feature_types and utilities queryset
            self.fields['feature_types'].queryset=ptype_obj.feature_type.all()
            self.fields['utility_bill'].queryset=ptype_obj.utilities.all()
            # self.fields['empty_set'].hidden=False
            # del self.fields['set_available'].widget


            if ptype_obj.name.lower() in ['bachelor','hostel']:
                # self.fields['ad_for'].choices=[('rb','Loking for Boy roommate'),('rs','Loking for Girl roommate')]
                self.hideAndDisabled('property_size')
                self.hideAndDisabled('bedroom')
                self.hideAndDisabled('living_room')



            else:
                # self.fields['ad_for'].choices=[('re','Rent'),('sa','Sale'),]
                self.hideAndDisabled('set_available')
                self.hideAndDisabled('roommate_type')
                # self.hideAndDisabled('hostal_type')
                self.hideAndDisabled('people_per_room')


    def hideAndDisabled(self,fieldName):
        self.fields[fieldName].widget=forms.HiddenInput()
        self.fields[fieldName].disabled=True

class PropertyImgForm(forms.Form):
    images=forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True,"class":'form-file-input'}),required=False)
    def save(self,*args,**kwargs):
        super(PropertyImg,self).save(*args,**kwargs)


class createContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        excludes=['id']

