from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Survey, Answer

# Create your views here.
def home(request):
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request,"home.html",{'survey':survey})


@csrf_protect
def save_survey(request):
    survey_idx = request.POST["survey_idx"]
    saver = Answer(survey_idx=request.POST["survey_idx"], ans=request.POST["num"])
    saver.save()
    return render(request,"success.html")


@csrf_protect
def show_result(request, question_id):
    answer = Answer.objects.filter(survey_idx=question_id)
    return render(request, "result.html",{'answer':answer})