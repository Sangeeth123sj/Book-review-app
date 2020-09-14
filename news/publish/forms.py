from django import forms
from .models import *
class contactForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField(label = 'Your email')
	comment = forms.CharField(widget=forms.Textarea)

class Picture_Form(forms.ModelForm):
	class Meta:
		model = Picture
		fields = ['picture']
