from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=200)
	price = models.IntegerField(default = 0)
	location = models.TextField(max_length=500)

class Order(models.Model):
	order_status = models.IntegerField(default=0)
	courses = models.ManyToManyField(Courses)
	user = models.ForeignKey(User)

