from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","teacher")
	search_fields = ("name","teacher__first_name","teacher__last_name")

admin.site.register(Course,CourseAdmin)
# Register your models here.
