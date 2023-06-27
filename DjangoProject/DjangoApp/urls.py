from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.login),
	# path('a/<int:id>/', views.a, name="sample"),
	path('', views.loginForm),
	path('reg/', views.regForm)
]