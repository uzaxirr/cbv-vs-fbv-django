from django.http import request
from django.shortcuts import render
from .models import Course
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from rest_framework.views import APIView
# Create your views here.

class ListCourse(APIView):

    def get(self, request):
        data = Course.objects.all()
        serialized_data = CourseSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        body_data = request.data
        serialized_course = CourseSerializer(data=body_data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data, status=status.HTTP_201_CREATED)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)




class CourseDetails(APIView):

    def get_object(self,request, pk):
        try:
            req_course = Course.objects.get(pk=pk)
            return req_course
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request, pk):
        req_course = self.get_object(request, pk=pk)
        serialized_course = CourseSerializer(req_course)
        return Response(serialized_course.data, status=status.HTTP_200_OK)

    def put(self,request, pk):
        body_data = request.data
        req_course = self.get_object(request,pk=pk)
        serialized_course = CourseSerializer(req_course, data=body_data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        req_course = self.get_object(request,pk=pk)
        req_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
