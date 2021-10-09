from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path('students/', student_list),
    path('student/<int:pk>', student_detail),
]
