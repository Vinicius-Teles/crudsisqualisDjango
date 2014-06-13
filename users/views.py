# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import UserForm
from datetime import datetime
from users.models import User
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
	formReturn = UserForm()
	if request.method == 'POST':		
		#Salvar
		form = UserForm(request.POST)
		formReturn = UserForm()
		if not form.data['id']:
			if form.is_valid():
				form.save()
			else:
				formReturn = form
		else: #atualizar
			server = get_object_or_404(User, pk=form.data['id'])
			form = UserForm(request.POST or None, instance=server)
			if form.is_valid():
				form.save()
			else:
				formReturn = form

	return render(request, 'users.html',{
		'form' : formReturn,
		'listUser' : User.objects.all()
	})
	

def delete(request, user_id):
	if request.method == 'POST':
		user = User.objects.get(pk=user_id)
		user.delete()
		return render(request, 'users.html',{
			'form' : UserForm(),
			'listUser' : User.objects.all()
		})
	else:
		return render(request, 'users.html',{
			'form' : UserForm(),
			'listUser' : User.objects.all()
		})

def update(request, user_id):
	if request.method == 'POST':
		user = User.objects.get(pk=user_id)
		return render(request, 'users.html',{
			'form' : UserForm(instance=user),
			'listUser' : User.objects.all(),
			'id' : user.id
		})

