from django.urls import path
from .views import ListStudents, GenStudentDetail

urlpatterns = [
    path('students', ListStudents.as_view()),
    path('student/<int:pk>', GenStudentDetail.as_view())
]
