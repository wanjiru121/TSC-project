from django.db import models
from course.models import Course
# from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# from student.validators import validate_domainonly_email


import datetime

class Student(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  date_of_birth = models.DateField(default=datetime.date.today)
  gender = models.CharField(max_length = 20)
  registration_number = models.CharField(max_length = 20)
  email = models.CharField(max_length = 70)
  phone_number = models.CharField(max_length = 15)
  date_joined = models.DateField()
  courses = models.ManyToManyField(Course,blank=True,related_name="students")
  image = models.ImageField(upload_to = "profile_image",blank = True)


  def __str__(self):
    return self.first_name + " " + self.last_name


  def full_name(self):
    return '{} {}'.format(self.first_name, self.last_name)
  
  def calculate_age(self):
    current_year = datetime.date.today().year
    return current_year - self.date_of_birth.year
  
  age = property(calculate_age)

  def clean(self):
    age = self.age
    if age < 17 or age > 30 : 
      raise ValidationError("You need to be above 17 years and below 30 years to register")
    return age



  
