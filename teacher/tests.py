from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse

import datetime

class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "gender": "female",
            "email": "janedoe@gmail.com",
            "phone_number": "0783982345",
            "profession": "Backend Developer",
            "date_joined": datetime.date(2019,2,2),
            "subject_training": "java",
            "id_number": "23456789"
        }

        self.bad_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "gender": "female",
            "email": "janedoe@gmail.com",
            "phone_number": "0783982345",
            "profession": "Backend Developer",
            "date_joined": "hello world",
            "subject_training": "java",
            "id_number": "23456789"
        }

    def test_teacher_form_always_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_teacher_form_always_reject_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())
    
    def test_add_teacher_view(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url,self.data)
        self.assertEqual(response.status_code,302)

    def test_add_teacher_view_with_bad_data(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url, self.bad_data)
        self.assertEqual(response.status_code, 400)