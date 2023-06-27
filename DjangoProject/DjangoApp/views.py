from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import hashlib

def hash(text):
	return (hashlib.sha256(text.encode())).hexdigest()

# Create your views here.

def a(request, id):
	# print(id)
	# return HttpResponse(f"<h3>Hello {id}</h3>")
	data = {
		'id': id
	}
	return render(request, "index.html", {'data': data})

def b(request):
	return render(request, "index.html")

def login(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user.objects.create(
			username = username,
			password = password
		).save()
		return HttpResponse(username + " " + password)
	else:
		return HttpResponse("There is no permission here")