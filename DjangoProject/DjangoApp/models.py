from django.db import models

# Create your models here.
class users(models.Model):
	id = models.CharField(max_length=11, primary_key=True)
	username = models.CharField(max_length=25)
	email = models.CharField(max_length=50, default="")
	password = models.CharField(max_length=100)