from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import GenStudent
from .serializers import GenStudentSerializer
from rest_framework import filters


class ListStudents(ListCreateAPIView):
    queryset = GenStudent.objects.all()
    serializer_class = GenStudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', '=score']

class GenStudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = GenStudent.objects.all()
    serializer_class = GenStudentSerializer