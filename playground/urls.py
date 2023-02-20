from django.urls import path
from . import views

#URL configurations
urlpatterns = [
	path('', views.simple_output),
	path('test/', views.anything)
]