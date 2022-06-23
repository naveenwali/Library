from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import *
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django.db import transaction


class CreateAdminAPIView(APIView):
	def post(self,request,*args,**kwargs):
		name = request.data.get('name')
		password = request.data.get('password')
		email = request.data.get('email')
		phone = request.data.get('phone')

		if Administrator.objects.filter(email=email).exists():
			msg = "user already existed"

			return Response(msg)

		else:
			admin = Administrator.objects.create(email=email,
										 name=name,
										 phone=phone,
										 password=password)

			return Response("success",status=HTTP_200_OK)


class StudentAPIView(APIView):
	def post(self,request,*args,**kwargs):
		name = request.data.get('name')
		password = request.data.get('password')
		email = request.data.get('email')
		phone = request.data.get('phone')
		roll_no = request.data.get('roll_no')

		if Student.objects.filter(email=email).exists():
			msg = "user already existed"
			return Response(msg)

		else:

			stud = Student.objects.create(email=email,
									  name=name,
									  password=password,
									  roll_no=roll_no,
									  phone=phone)

			return Response("success",status=HTTP_200_OK)


class AdministratorLoginAPIView(APIView):
	def post(self,request,*args,**kwargs):
		email = request.data.get('email')
		password = request.data.get('password')

		if Administrator.objects.filter(email=email).exists():
			print('hiii')
			admin = Administrator.objects.get(email=email)
			print('hiiiiiiiiiiiiii')
			if admin.password == password:
				print("hellooo")
				return Response('success',status=HTTP_200_OK)
			else:
				return Response('incorrect',status=HTTP_400_BAD_REQUEST)

		else:
			msg = "Administrator does not exists"

			return Response(msg,status=HTTP_400_BAD_REQUEST)


class StudentLoginAPIView(APIView):
	def post(self,request,*args,**kwargs):
		email = request.data.get('email')
		password = request.data.get('password')

		if Student.objects.filter(email=email).exists():
			stu = Student.objects.get(email=email)
			if stu.password == password:
				return Response('success',status=HTTP_200_OK)
			else:
				return Response('incorrect',status=HTTP_400_BAD_REQUEST)
		else:
			msg = "Student does not exists"
			return Response(msg,status=HTTP_400_BAD_REQUEST)


class CreateBooksAPIView(APIView):
	def post(self,request):

		serializers = BookSerializer(data=request.data)
		print(serializers)
		if serializers.is_valid(raise_exception=True):
			book_obj = serializers.save()

			return Response("success",status=HTTP_200_OK)

		return Response(serializers.error,status=HTTP_400_BAD_REQUEST)

	def get(self,request):
		book = Book.objects.all()
		serializers = BookSerializer( book, many=True)
		return Response(serializers.data,status=HTTP_200_OK)

class BookDelandUpAPIView(APIView):
	def put(self,request,b_id):
		book = Book.objects.get(pk=b_id)
		serializers = BookSerializer(book,data=request.data)
		if serializers.is_valid(raise_exception=True):
			book_obj = serializers.save()

			return Response("success",status=HTTP_200_OK)

		return Response(serializers.error,status=HTTP_400_BAD_REQUEST)

	def delete(self,request,b_id):
		book_obj = Book.objects.filter(pk=b_id).delete()

		return Response(book_obj,status=HTTP_200_OK)

