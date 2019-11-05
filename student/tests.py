from django.test import TestCase
from .models import Student
from  student.forms import StudentForm
from django.test import Client
from django.urls import reverse
import datetime


class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name = 'Rose',
            last_name = 'Wanjiku',
            date_of_birth = datetime.date(1998,8,23),
            gender = 'female',
            registration_number = '7552',
            email = 'rosewanjiru121@gmail.com',
            date_joined = datetime.date.today(),
            )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())


    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())

    def test_age_is_always_above_17(self):
        self.assertFalse(self.student.clean() < 17 )
    
    def test_age_is_always_below_30(self):
        self.assertFalse(self.student.clean() > 30)

        

class AddStudentTestCase(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Rose",
            "last_name": "Wanjiku",
            "date_of_birth": datetime.date(1998,8,23),
            "gender": "female",
            "registration_number": "7552",
            "email": "rosewanjiru121@gmail.com",
            "phone_number": "0797564719",
            "date_joined": datetime.date(2019,2,2)
        }

        self.bad_data =  {
            "first_name": "Rose",
            "last_name": "Wanjiku",
            "date_of_birth": "hello",
            "gender": "female",
            "registration_number": "7552",
            "email": "rosewanjiru121@gmail.com",
            "date_joined": datetime.date(2019,2,2)	
        }
    
    def test_student_form_accepts_valid_data(self):
        form = StudentForm(self.data)
        self.assertTrue(form.is_valid())

    def test_student_form_always_reject_invalid_data(self):
        form = StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())
    
    def test_add_student_view(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url, self.data)
        self.assertEqual(response.status_code,302)
    
    def test_add_student_view_with_bad_data(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url,self.bad_data)
        self.assertEqual(response.status_code, 400)

    def test_update_result(self):
        student = Student.objects.create(first_name="Rose",last_name="Wanjiku",date_joined=datetime.date.today())
        Student.objects.filter(first_name="Rose").update(first_name="Shee")
        student.refresh_from_db()
        self.assertEqual(student.first_name,"Shee")



# Create your tests here.
