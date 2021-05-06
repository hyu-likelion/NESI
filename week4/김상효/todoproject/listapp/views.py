from django.shortcuts import render, redirect
from .forms import TodoPost
from .models import Todo


def home(request):
    todo_list = Todo.objects.all()
    form = TodoPost()
    return render(request, 'home.html', {'form': form, 'todo_list': todo_list})


def new(request):
    todo = TodoPost(request.POST)
    if todo.is_valid:
        todo.save()
        return redirect('home')


def edit(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoPost(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
        return redirect('home')

    else:
        return render(request, 'edit.html', {'todo': todo})


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')
