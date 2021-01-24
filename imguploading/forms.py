
from django import forms
from .models import *

class HotelForm(forms.ModelForm):
	images=forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model = Hotel
		fields = ['name', 'images']
