from django.forms import ModelForm
from users.models import User, Category
from django import forms
from datetime import datetime

class UserForm(ModelForm):
	anniversaryDate = DateField(input_formats=settings.DATE_INPUT_FORMATS)
	class Meta:
		model = User
		fields = '__all__'