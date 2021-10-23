from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers
from rest_framework import status
from .models import TaskModel
from .serializers import TaskSerializer


class TaskListUser(APIView):
	"""
	Вывод и добавление записей пользователя
	"""
	permission_classes = [permissions.IsAuthenticated,]
	
	def get(self, request):
		"""
			Вывод записей пользователя по id пользователя
		"""
		tasks = TaskModel.objects.filter(user=request.user)
		serializer = TaskSerializer(tasks, many=True)
		return Response(serializer.data)
	
	def post(self, request):
		serializers = TaskSerializer(data=request.data)
		if serializers.is_valid():
			serializers.save(user=request.user)
			return Response(serializers.data, status=status.HTTP_201_CREATED)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



