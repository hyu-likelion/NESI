from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')

def calculator(request):
    a = request.GET['eq']
    b = eval(a)


    return render(request,'calculator.html',{'result' : b})
