from django.contrib import admin

# from studentapi.app.models import Student

# Register your models here.
from app.models import Student,Course
admin.site.register(Student)
admin.site.register(Course)