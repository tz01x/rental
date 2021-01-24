from django import forms
from .models import  *
class featureFrom(forms.ModelForm):
    types=forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=FeatureType.objects.all(),
    )
    class Meta:
        model=Features
        fields=['types']
        exclude=['id']
    def __init__(self,*args,**kwargs):
        ptypeId=kwargs.pop('ptypeId',None)
        super(featureFrom,self).__init__(*args, **kwargs)
        if(ptypeId is not None):
            self.fields['types'].queryset=FeatureType.objects.filter(ptype=ptypeId)
