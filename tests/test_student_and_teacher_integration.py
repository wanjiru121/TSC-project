from django.test import TestCase
from teacher.models import Teacher
from student.models import Student
from course.models import Course
import datetime



class TeacherStudentTestCase(TestCase):
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

        self.student_a = Student.objects.create(
            first_name = 'Rose',
            last_name = 'Wanjiku',
            date_of_birth = datetime.date(1998,8,23),
            gender = 'female',
            registration_number = '7552',
            email = 'rosewanjiru121@gmail.com',
            date_joined = datetime.date.today(),
            )
        self.student_b = Student.objects.create(
            first_name = 'Esther',
            last_name = 'Njoki',
            date_of_birth = datetime.date(2007,7,6),
            gender = 'female',
            registration_number = '7652',
            email = 'esthernjoki@gmail.com',
            date_joined = datetime.date.today(),
            )



    # def test_a_trainer_and_many_students_can_belong_to_one_course(self):
    #     self.student_a.courses.add(self.python)
    #     self.student_b.courses.add(self.python)
    #     self.python.teacher = self.teacher_b
        
    