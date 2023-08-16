from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):

	class Meta:
		model = Notes
		fields = ('title','notes')
		widgets = {
		'title' : forms.TextInput(attrs = {'class':'form-control','placeholder':'enter a title',}),
		'notes': forms.Textarea(attrs = {'class' : 'form-control','placeholder':'Enter some content ',})
		} 
		labels = {
		'text' : "Write Your thoughts here"
		}

	def clean_title(self):
		title = self.cleaned_data['title']
		if 'Django' not in title:
			raise ValidationError('We only accept notes about django')
		return title