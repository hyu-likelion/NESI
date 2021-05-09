from django.shortcuts import render,redirect
from .models import TODO
from .forms import Todoform

def home(request):
    form=Todoform()
    todo=TODO.objects.all()
    return render(request,'home.html',{'todo':todo,'form':form})

def create(request):
   if request.method=='POST':
       form=Todoform(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')

def edit(request,id):
    edit_list=TODO.objects.get(id=id)
    return render(request,'edit.html',{'todo':edit_list})

def update(request,id):
    if request.method=='POST':
        update_td=TODO.objects.get(id=id)
        form=Todoform(request.POST, instance=update_td)
        if form.is_valid():
            form.save()
            return redirect('home')

def delete(request,id):
    delete_todo=TODO.objects.get(id=id)
    delete_todo.delete()
    return redirect('home')