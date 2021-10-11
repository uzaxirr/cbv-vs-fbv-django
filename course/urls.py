from django.urls import path
from .views import CourseDetails, ListCourse
urlpatterns = [
    path('courses', ListCourse.as_view()),
    path('course/<int:pk>', CourseDetails.as_view()),
]
