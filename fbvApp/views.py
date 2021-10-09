from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        input_data = request.data
        serialized_data = StudentSerializer(data=input_data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_detail(request, pk):
    body_data = request.data

    try:
        req_student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serialized_stu = StudentSerializer(req_student)
        return Response(serialized_stu.data)

    if request.method == 'PUT':
        serialized_stu = StudentSerializer(req_student, data=body_data)
        if serialized_stu.is_valid():
            serialized_stu.save()
            return Response(serialized_stu.data, status=status.HTTP_201_CREATED)
        return Response(serialized_stu.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        req_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)