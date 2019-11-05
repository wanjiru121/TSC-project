# Generated by Django 2.2.1 on 2019-10-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20191001_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]