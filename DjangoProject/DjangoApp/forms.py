from django.forms import ModelForm, PasswordInput, CharField
from .models import *

class usersForm(ModelForm):
	class Meta:
		model = user
		fields = '__all__'
