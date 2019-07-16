from django.contrib import admin

from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","subject_training","email","profession")
	search_fields = ("first_name","last_name","email","subject_training")
admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
