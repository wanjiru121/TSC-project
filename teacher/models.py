from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    email = models.CharField(max_length = 70)
    phone_number = models.CharField(max_length = 15)
    profession = models.CharField(max_length = 100)
    date_joined = models.DateField()
    subject_training = models.CharField(max_length = 50)
    id_number = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    # Create your models here.
