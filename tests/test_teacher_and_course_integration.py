from django.test import TestCase
from teacher.models import Teacher
from course.models import Course
import datetime


class TeacherCourseTestCase(TestCase):
    def setUp(self):
        self.teacher_a = Teacher.objects.create(
            first_name = "Jane",
            last_name = "Doe",
            gender = "female",
            email = "janedoe@gmail.com",
            phone_number = "0783982345",
            profession = "Backend Developer",
            date_joined = datetime.date(2019,2,2),
            subject_training = "java",
            id_number= "23456789"
        )   
        self.teacher_b = Teacher.objects.create(
            first_name = "John",
            last_name = "Doe",
            gender = "male",
            email = "johndoe@gmail.com",
            phone_number = "0703982345",
            profession = "Android Developer",
            date_joined = datetime.date(2019,2,2),
            subject_training = "JS",
            id_number= "23456709"
        )  
        self.python = Course.objects.create(
            name = "Python",
            duration_in_months = 10,
            start_date = datetime.date(2019,2,2),
            end_date = datetime.date(2019,11,30),
            description = "My favourite",
        )

        self.javascript = Course.objects.create(
            name = "javascript",
            duration_in_months = 10,
            start_date = datetime.date(2019,2,2),
            end_date = datetime.date(2019,11,30),
            description = "My second favourite" 
        )

        self.java = Course.objects.create(
            name = "java",
            duration_in_months = 10,
            start_date = datetime.date(2019,2,2),
            end_date = datetime.date(2019,11,30),
            description = "My third favourite" 
        )


    def test_course_can_be_trained_by_a_teacher(self):
        self.python.teacher = self.teacher_a
        self.assertEqual(self.python.teacher, self.teacher_a)

    
    def test_many_courses_can_be_trained_by_one_trainer(self):
        self.python.teacher = self.teacher_b
        self.java.teacher = self.teacher_b
        self.assertEqual(self.java.teacher,self.python.teacher)
    