from rest_framework import serializers
from .models import *

class AdministratorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Administrator
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'
