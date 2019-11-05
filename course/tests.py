from django.test import TestCase
from .models import Course
from course.forms import CourseForm
from django.test import Client
from django.urls import reverse
import datetime


class AddCourseTestCase(TestCase):
    def setUp(self):
        self.data = {
            "name": "Java",
            "duration_in_months": 10,
            "start_date": datetime.date(2019,2,2),
            "end_date": datetime.date(2019,10,10),
            "description": "Really interesting"
        }

        self.bad_data = {
            "name": "Java",
            "duration_in_months": "10",
            "start_date": datetime.date(2019,2,2),
            "end_date": "yoh",
            "description": "Really interesting"
        }

    def test_course_form_always_accepts_valid_data(self):
        form = CourseForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_course_form_always_rejects_invalid_data(self):
        form = CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_course_view(self):
        client = Client()
        url = reverse("add_course")
        response = client.post(url,self.data)
        self.assertEqual(response.status_code, 302)

    def test_add_course_view_with_bad_data(self):
        client = Client()
        url = reverse("add_course")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)