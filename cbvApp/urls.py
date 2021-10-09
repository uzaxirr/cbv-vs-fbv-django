from django.urls import path
from .views import ListStudents, DetailedStudent

urlpatterns = [
    path('students/', ListStudents.as_view()),
    path('student/<int:pk>', DetailedStudent.as_view())
]