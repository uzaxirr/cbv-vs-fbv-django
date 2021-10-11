from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import GenStudent

class GenStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenStudent
        fields = '__all__'