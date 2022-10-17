from django.shortcuts import render,redirect
from django.http import HttpResponse
from TODOapp.forms import Empform
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"temp/base.html")

def index(request):
    emp_data = EmpdataModel.objects.all()
    context = {
        "emp_data":emp_data
    }
    return render(request,"temp/index.html",context)
def add_emp(request):
    form = Empform
    if request.method == "POST":
        form=Empform(request.POST)
        print("form is valid")
        form.save()
        messages.info(request,"Employee data added successfully")
    else:
        pass
    emp_data = EmpdataModel.objects.all()
    context = {
        "emp_data":emp_data
    }
    return render(request,"temp/index.html",context,{"form":form})

def emp_del(request,emp):
    emp_data = EmpdataModel.objects.get(id=emp)
    emp_data.delete()
    messages.info(request,"Employee data deleted successfully")
    return redirect(index)

def emp_edit(request,emp):
    set_data = EmpdataModel.objects.get(id=emp)
    data = EmpdataModel.objects.all()
    context = {
        "set_data":set_data,
        "data":data
    }
    return render(request,"temp/index.html",context)

def emp_update(request,emp):
    set_data = EmpdataModel.objects.get(id=emp)
    form = Empform(request.POST,instance=set_data)
    if form.is_valid():
        print("data updated")
        form.save()
        messages.info(request,"Employee data updated successfully")
        return redirect("index")
    return render(request,"index.html")