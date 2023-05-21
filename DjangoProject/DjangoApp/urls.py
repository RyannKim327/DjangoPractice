from django.urls import path
from . import views

urlpatterns = [
	path('a/<int:id>/', views.a, name="sample"),
	path('', views.b)
]