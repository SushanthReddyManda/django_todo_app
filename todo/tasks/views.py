from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = model_class.objects.all()
    form = model_class_form()
    if request.method == 'POST':
        form  = model_class_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'task_dict':tasks, 'form_dict':form}
    return render(request,"list.html", context)

def  update_task(request, pk):
    task = model_class.objects.get(id = pk)
    form = model_class_form(instance = task)
    if request.method == 'POST':
        form = model_class_form(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form_dict' : form}
    return render(request,"update.html", context)

def  delete_item(request, pk):
    item = model_class.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context  = {'item_name': item}
    return render(request,"delete_item.html", context)