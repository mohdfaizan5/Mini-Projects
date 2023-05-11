from django.db import models

# Create your models here.

GENDER = [
    ("male", "MALE" ),
    ("female", "FEMALE")
]

class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=80)
    # first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    gpa = models.FloatField(max_length=10, null=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True)

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"

# ds
