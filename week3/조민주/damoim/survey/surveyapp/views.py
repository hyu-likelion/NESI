from django.shortcuts import render,redirect
from .models import Name
from .forms import NameForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def create_name(request):
    form = NameForm()
    return render(request,"name.html",{'form':form})

def save_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form = form.save()   
            return redirect('result')
        else:
            return redirect('result')
    else: 
        form = NameForm()
        return render(request,"result.html",{'form':form})

def result(request):
    results = Name.objects.all()
    print(results,"name")
    return render(request,'result.html',{'results':results})


#def hobby(request):
    #hobbies =  Hobby.objects.all()
    #return render(request, "hobby.html")

#def save_hobby(request):
    save_hobbies = Saver(name=request.POST["num"])

#def result(request):
