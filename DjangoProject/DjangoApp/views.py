from django.shortcuts import render
from django.http import HttpResponse

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