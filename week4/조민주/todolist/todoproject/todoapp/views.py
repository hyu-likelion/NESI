from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import datetime
from .models import Todo
from .forms import TodoForm


# Create your views here.
def home(request):
    todo = Todo.objects.all()
    form = TodoForm()
    return render(request, 'home.html', {'todo':todo, 'form':form})

def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at=datetime.now()
            post.save() 
            return redirect('home')
        else:
            return redirect('home')
    else: 
        form = TodoForm()
        return render(request,"home.html",{'todo':form})


def edit(request,id):
    edit_todo = Todo.objects.get(id=id)
    return render(request,'edit.html',{'todo':edit_todo})

def update(request,id):
    post = get_object_or_404(Todo,id=id)
    post.todolist = request.POST['todolist']
    post.save()
    return redirect('home')

def delete(request,id):
    form = get_object_or_404(Todo,id=id)
    if id == form.id:
        form.delete()
        return redirect('home')

