from django.shortcuts import render
from django.viws import generic
# Create your views here.

from .models import * 
class Index(generic.ListView):
	queryset = Blog.
