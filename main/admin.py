from django.contrib import admin
from django import forms
from .models import Student,SelectedStd
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display=['Roll_No','Name','F_Name','Address','Marks','Contact','FIELDS','Condition','Selected']
	list_filter=['FIELDS','Condition','Selected']


admin.site.register(Student,StudentAdmin)

class SelectedStdAdmin(admin.ModelAdmin):
	list_display=['Roll_No','Name','F_Name','Address','Marks','Contact','FIELDS','Condition','Selected']
	list_filter=['Condition','FIELDS']


admin.site.register(SelectedStd,SelectedStdAdmin)
