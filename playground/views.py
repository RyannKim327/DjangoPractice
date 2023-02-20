from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request --> response

def simple_output(req):
	# return HttpResponse("Hello World")
	return render(req, 'simple_documentation.html')

def anything(req):
	return render(req, 'index.html', {'name': "Sample"})