# Generated by Django 2.2.1 on 2019-06-12 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_remove_teacher_upload_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='number_of_subjects',
        ),
    ]
