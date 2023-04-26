from django import forms
from main.models import Student

class AddStudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['Roll_No','Name','F_Name','Address','Marks','Condition','Contact','FIELDS','Condition']
