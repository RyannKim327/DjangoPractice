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

def loginForm(request):
	return render(request, "index.html")

def register(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = hash(request.POST.get('password', ''))
		user.objects.create(
			username = username,
			password = password
		).save()
		return HttpResponse(f"{username} {password}")
	else:
		return render(request, "registration.html")

def login(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username', '')
			password = hash(request.POST.get('password', ''))
			d = user.objects.get(username__exact=username)
			if password == d.password:
				return render(request, "index.html", { "data": {
					"msg": "Wrong username or password"
				}})
			else:
				return render(request, "index.html", { "data": {
					"msg": "Wrong username or password"
				}})
		except:
			return render(request, "index.html", { "data": {
				"msg": "Wrong username or password"
			}})
	return render(request, "index.html", { "data": {
		'msg': "Welcome user"
	}})