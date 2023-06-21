from django.forms import ModelForm
from .models import *

class usersForm(ModelForm):
	
	class Meta:
		model = users
		fields = '__all__'
