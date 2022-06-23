from django.db import models
# Create your models here.
# from datetime import datetime,timedelta


class Administrator(models.Model):
	email = models.EmailField(unique=True, blank=False, null=False)
	password = models.CharField(max_length=12, blank=False, null=False)
	name = models.CharField(max_length=20)
	phone = models.CharField(max_length=10)
	def __str__(self):
		return str(self.name) + " ["+str(self.email)+']'

class Student(models.Model):
	email = models.EmailField(unique=True, blank=False, null=False)
	password = models.CharField(max_length=12, blank=False, null=False)
	name = models.CharField(max_length=12)
	roll_no = models.CharField(max_length=3)
	phone = models.CharField(max_length=10)

	def __str__(self):
		return str(self.name) + " ["+str(self.roll_no)+']'
 
class Book(models.Model):
	name = models.CharField(max_length=20)
	author = models.CharField(max_length=50)
	book_num = models.PositiveIntegerField()
	category = models.CharField(max_length=50)

	def __str__(self):
		return str(self.name) + " ["+str(self.book_num)+']'

