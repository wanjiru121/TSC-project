from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime



class StudentCourseTestCase(TestCase):
    def setUp(self):
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
        self.python = Course.objects.create(
            name = "Python",
            duration_in_months = 10,
            start_date = datetime.date(2019,2,2),
            end_date = datetime.date(2019,11,30),
            description = "My favourite" 
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
    def test_student_can_join_a_course(self):
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(), 1)

    def test_student_can_join_many_course(self):
            self.student_a.courses.add(self.python,self.javascript,self.java)
            self.assertEqual(self.student_a.courses.count(), 3)