# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200) 
	description = models.TextField()

	def __str__(self):
		return self.name


class User(models.Model):
	name = models.CharField(max_length=200)
	anniversaryDate = models.DateField('anniversaryDate')
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.name