from django.forms import ModelForm
from users.models import User, Category
from django import forms

class UserForm(ModelForm):

	class Meta:
		model = User
		fields = '__all__'