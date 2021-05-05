from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, id=id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    nb=Blog()
    nb.title= request.POST['title']
    nb.writer=request.POST['writer']
    nb.body=request.POST['body']
    nb.pub_date=timezone.now()
    nb.save()
    return redirect('detail',nb.id)
def edit(request,id):
    eb=Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':eb})
def update(request,id):
    ub=Blog.objects.get(id=id)
    ub.title = request.POST['title']
    ub.writer = request.POST['writer']
    ub.body = request.POST['body']
    ub.pub_date = timezone.now()
    ub.save()
    return redirect('detail',ub.id)

def delete(request,id):
    db=Blog.objects.get(id=id)
    db.delete()
    return redirect('home')