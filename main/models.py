from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
	id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	Conditions=[('OPEN','OPEN'),('LOCAL','LOCAL'),]
	FIELD1_S=[('Medical','Medical'),('Engineering','Engineering'),('Computer Science','Computer Science'),('Humanities','Humanities'),]
	Name=models.CharField(max_length=100)
	F_Name=models.CharField(max_length=100)
	Roll_No=models.PositiveIntegerField()
	Address=models.CharField(max_length=100,blank=False)
	Marks=models.PositiveIntegerField()
	Contact=models.PositiveIntegerField()
	FIELDS=models.CharField(max_length=20,choices=FIELD1_S,default='Medical')
	Condition=models.CharField(max_length=10,choices=Conditions,default='OPEN')
	Entry_Date=models.DateTimeField(default=timezone.now())
	Selected=models.BooleanField(null=True,blank=True,default=False)
	Selected_Date=models.DateTimeField(null=True,blank=True)

	def selected1(self):
		self.Selected=True
		self.Selected_Date=timezone.now()
		self.save()


	class Meta:
		ordering=('-Marks',)

	def __str__(self):
		return str(self.id)


class SelectedStd(models.Model):
	id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	Conditions=[('OPEN','OPEN'),('LOCAL','LOCAL'),]
	FIELD1_S=[('Medical','Medical'),('Engineering','Engineering'),('Computer Science','Computer Science'),('Humanities','Humanities')]
	Name=models.CharField(max_length=100)
	F_Name=models.CharField(max_length=100)
	Roll_No=models.PositiveIntegerField()
	Address=models.CharField(max_length=100)
	Marks=models.PositiveIntegerField()
	Contact=models.PositiveIntegerField()
	FIELDS=models.CharField(max_length=20,choices=FIELD1_S)
	Condition=models.CharField(max_length=10,choices=Conditions,default='OPEN')
	Entry_Date=models.DateTimeField(default=timezone.now())
	Selected=models.BooleanField(default=True)
	Selected_Date=models.DateTimeField(null=True,blank=True)

	def deselect(self):
		self.Selected=False
		self.save()

	class Meta:
		ordering=('-Marks',)

	def __str__(self):
		return str(self.id)
