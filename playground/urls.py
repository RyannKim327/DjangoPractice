from django.urls import path
from . import views

#URL configurations
urlpatterns = [
	path('test/', views.anything)
]