from django.db import reset_queries
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from cbvApp.models import Student
from fbvApp.serializers import StudentSerializer
from rest_framework import status
# Create your views here.

class ListStudents(APIView):

    def get(self, request):
        data = Student.objects.all()
        serialized_stu = StudentSerializer(data, many=True)
        return Response(serialized_stu.data)
    
    def post(self, request):
        body_data = request.data
        serialized_stu = StudentSerializer(data=body_data)
        if serialized_stu.is_valid():
            serialized_stu.save()
            return Response(serialized_stu.data, status=status.HTTP_201_CREATED)
        return Response(serialized_stu.errors, status=status.HTTP_400_BAD_REQUEST)



class DetailedStudent(APIView):
    
    def get_object(self,pk):
        try:
            req_stu = Student.objects.get(pk = pk)
            return req_stu
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serialized_stu = StudentSerializer(student)
        return Response(serialized_stu.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        body_data = request.data
        req_stu = self.get_object(pk=pk)
        serialized_stu = StudentSerializer(req_stu, data=body_data)
        if serialized_stu.is_valid():
            serialized_stu.save()
            return Response(serialized_stu.data)
        return Response(serialized_stu.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        req_student = self.get_object(pk=pk)
        req_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
