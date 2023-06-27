from django.db import models

# Create your models here.
class user(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=25)
	email = models.CharField(max_length=50, default="")
	password = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.username} {self.email}"