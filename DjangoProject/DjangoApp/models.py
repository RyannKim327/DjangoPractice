from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"


class msg(models.Model):
    userID = models.IntegerField(max_length=11, null=False)
    message = models.CharField(max_length=9999, null=False)
    delivery = models.IntegerField(max_length=99, default=0)

    def __str__(self):
        return f"{self.username}: {self.message}\n{self.delivery}"
