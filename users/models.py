# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200)
	anniversaryDate = models.DateField('anniversaryDate')

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200) 
	description = models.TextField()
	users = models.ManyToManyField(User)

	def __str__(self):
		return self.name