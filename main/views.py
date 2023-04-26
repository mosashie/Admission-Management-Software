from django.shortcuts import render,redirect,get_object_or_404
from main.models import Student,SelectedStd
from main.forms import AddStudentForm
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

def add_std(request):
	if request.method=='POST':
		form=AddStudentForm(request.POST)
		if form.is_valid():
			form.save()
			form=AddStudentForm()
			a='Record Added Successfully'
			return render(request,'main/add_std.html',{'form':form,'a':a})

	else:
		form=AddStudentForm()
	return render(request,'main/add_std.html',{'form':form})


def list_view(request):
	students=Student.objects.filter(Condition='OPEN')
	return render(request,'main/students_list.html',{'students':students})
#this is start of local
def local_eng(request):
	students=Student.objects.filter(Condition='LOCAL',FIELDS='Engineering')
	return render(request,'main/local_eng.html',{'students':students})
def select5(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:local_eng')


def delete6(request,pk):
	eng2=get_object_or_404(Student,pk=pk)
	eng2.delete()
	return redirect('main:local_eng')

def local_med(request):
	students=Student.objects.filter(Condition='LOCAL',FIELDS='Medical')
	return render(request,'main/local_med.html',{'students':students})

def delete7(request,pk):
	eng2=get_object_or_404(Student,pk=pk)
	eng2.delete()
	return redirect('main:local_med')
def select6(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:local_med')


def local_comp(request):
	students=Student.objects.filter(Condition='LOCAL',FIELDS='Computer Science')
	return render(request,'main/local_cs.html',{'students':students})

def delete8(request,pk):
	eng2=get_object_or_404(Student,pk=pk)
	eng2.delete()
	return redirect('main:local_cs')

def select7(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:local_cs')


def local_hum(request):
	students=Student.objects.filter(Condition='LOCAL',FIELDS='Humanities')
	return render(request,'main/local_hum.html',{'students':students})

def delete9(request,pk):
	eng2=get_object_or_404(Student,pk=pk)
	eng2.delete()
	return redirect('main:local_hum')

def select8(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:local_hum')



#this is end of local..

#selected student not local start
def selected_view(request):
	studentselected=Student.objects.filter(Selected=True)
	selectedstd1=SelectedStd()
	for std in studentselected:
		selectedstd1.id=std.id
		selectedstd1.Roll_No=std.Roll_No
		selectedstd1.Name=std.Name
		selectedstd1.F_Name=std.F_Name
		selectedstd1.Address=std.Address
		selectedstd1.Marks=std.Marks
		selectedstd1.Contact=std.Contact
		selectedstd1.FIELDS=std.FIELDS
		selectedstd1.Condition=std.Condition
		selectedstd1.Entry_Date=std.Entry_Date
		selectedstd1.Selected=std.Selected
		selectedstd1.Selected_Date=std.Selected_Date
		selectedstd1.save()
	students=Student.objects.filter(Selected=True,Condition='OPEN')
	return render(request,'main/selected_list.html',{'students':students})

def med_slct(request):
	students=Student.objects.filter(Selected='True',Condition='OPEN',FIELDS='Medical')
	return render(request,'main/med_slct.html',{'students':students})

def eng_slct(request):
	students=Student.objects.filter(Selected='True',Condition='OPEN',FIELDS='Engineering')
	return render(request,'main/eng_slct.html',{'students':students})

def cs_slct(request):
	students=Student.objects.filter(Selected='True',Condition='OPEN',FIELDS='Computer Science')
	return render(request,'main/cs_slct.html',{'students':students})

def hum_slct(request):
	students=Student.objects.filter(Selected='True',Condition='OPEN',FIELDS='Humanities')
	return render(request,'main/hum_slct.html',{'students':students})
#selected students not local ended

#start of local selected students

def all_local_slct(request):
	students=Student.objects.filter(Selected='True',Condition='LOCAL')
	return render(request,'main/all_local_slct.html',{'students':students})

def med_local_slct(request):
	students=Student.objects.filter(Selected='True',Condition='LOCAL',FIELDS='Medical')
	return render(request,'main/med_local_slct.html',{'students':students})

def eng_local_slct(request):
	students=Student.objects.filter(Selected='True',Condition='LOCAL',FIELDS='Engineering')
	return render(request,'main/eng_local_slct.html',{'students':students})

def cs_local_slct(request):
	students=Student.objects.filter(Selected='True',Condition='LOCAL',FIELDS='Computer Science')
	return render(request,'main/cs_local_slct.html',{'students':students})

def hum_local_slct(request):
	students=Student.objects.filter(Selected='True',Condition='LOCAL',FIELDS='Humanities')
	return render(request,'main/hum_local_slct.html',{'students':students})

#end of local selected students

def medical_std(request):
	medical1=Student.objects.filter(FIELDS='Medical',Condition='OPEN')
	return render(request,'main/MedicalStudents.html',{'students':medical1})

def Engr_std(request):
	engr=Student.objects.filter(FIELDS='Engineering',Condition='OPEN')
	return render(request,'main/Engineering.html',{'students':engr})

def cs_std(request):
	cs=Student.objects.filter(FIELDS='Computer Science',Condition='OPEN')
	return render(request,'main/ComputerScience.html',{'students':cs})

def hum_std(request):
	hum=Student.objects.filter(FIELDS='Humanities',Condition='OPEN')
	return render(request,'main/Humanite.html',{'students':hum})


def select1(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:medical_std')


def select2(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:Engr_std')

def select3(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:cs_std')

def select4(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.selected1()
	return redirect('main:hum_std')


def delete1(request,pk):
	std1=get_object_or_404(Student,pk=pk)
	std2=get_object_or_404(SelectedStd,pk=pk)
	std1.delete()
	std2.delete()
	return redirect('main:selected_view')

def delete2(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.delete()
	return redirect('main:medical_std')

def delete3(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.delete()
	return redirect('main:Engr_std')

def delete4(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.delete()
	return redirect('main:cs_std')

def delete5(request,pk):
	std=get_object_or_404(Student,pk=pk)
	std.delete()
	return redirect('main:hum_std')

def search(request):
	if request.method=='POST':
		search1=request.POST['srch']

		if search1:
			match1=Student.objects.filter(Q(Roll_No__iexact=search1)|Q(Name__iexact=search1))
			if match1:
				return render(request,'main/search.html',{'search11':match1})
			else:
				return render(request,'main/search.html',{'error':'Search Not Found'})
		else:
			return redirect('main:search')
	else:
		return render(request,'main/search.html')
