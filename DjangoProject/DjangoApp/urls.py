from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.loginForm),
	path('a/<int:id>/', views.a, name="sample"),
	path('', views.login),
	path('reg/', views.regForm)
]