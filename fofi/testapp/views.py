from django.shortcuts import render
from testapp.forms import StudentForm
from testapp.models import Student
from . import forms

# Create your views here.
def home(request):
    return render(request,"testapp/base.html")
def student_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'testapp/studentform.html',{'form':form})

def list(request):
    movie_list=Student.objects.all()
    return render(request,"testapp/list.html",{"movie_list":movie_list})