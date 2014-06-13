# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import UserForm

# Create your views here.


def index(request):
	if request.method == 'POST':
		pass
	else:
		form = UserForm()
	return render(request, 'teste.html',{
			'form' : form
		})

