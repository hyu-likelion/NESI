from django.shortcuts import render
from .models import Surv, Answer

def home(request):
    test=Surv.objects.filter(valid='y').order_by('-surv_idx')[0]
    return render(request,'list.html',{'test':test})

def save_surv(request):
    store=Answer(surv_idx=int(request.POST['s_idx']),ans=request.POST['num'])
    store.save()
    return render(request,'success.html')

def result(request, question_id):
    result=Answer.objects.filter(surv_idx=question_id)
    return render(request,'result.html',{'result':result})
