# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import UserForm
from datetime import datetime
from users.models import User

# Create your views here.


def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'users.html',{
				'listUser' : User.objects.all()
			})
	else:
		form = UserForm()
	return render(request, 'users.html',{
			'form' : form,
			'listUser' : User.objects.all()
		})

