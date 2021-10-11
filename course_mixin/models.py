from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=250)
    rating = models.IntegerField()

    def __self__(self):
        return self.name