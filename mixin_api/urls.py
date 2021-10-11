from django.urls import path

from mixin_api.views import MixListStudents, MixStudentDetails

urlpatterns = [
    path('students/', MixListStudents.as_view()),
    path('student/<int:pk>', MixStudentDetails.as_view())
]