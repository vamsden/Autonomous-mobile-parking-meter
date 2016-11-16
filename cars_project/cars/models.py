from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=64)
	address = models.CharField(max_length=30, default="Australia")
	email = models.CharField(max_length=30)
	phone_number = models.IntegerField()

	def __str__(self):
		return self.username


class Vehicle(models.Model):
	owners = models.ForeignKey(User, on_delete=models.CASCADE)
	manufacturer = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	vehicle_number = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.vehicle_number