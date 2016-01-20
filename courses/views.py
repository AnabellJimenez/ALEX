from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from items.models import Items, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def courses(request):
	return HttpResponse("these are the courses")