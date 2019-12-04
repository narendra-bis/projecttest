from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
	print('indextest')
	return render(request,'myapp/index.html')
