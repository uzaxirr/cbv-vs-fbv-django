from django.urls import path
from .views import MixListCourse, MixCourseDetail

urlpatterns = [
    path('courses/', MixListCourse.as_view()),
    path('course/<int:pk>', MixCourseDetail.as_view()),
]
