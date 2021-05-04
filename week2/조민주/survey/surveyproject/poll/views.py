from django.shortcuts import render
from .models import Survey, Answer

# Create your views here.
def home(request):
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request,"home.html",{'survey':survey})


def save_survey(request):
    survey_idx = request.POST["survey_idx"]
    saver = Answer(survey_idx=request.POST["survey_idx"], ans=request.POST["num"])
    saver.save()
    return render(request,"success.html")

def show_result(request, question_id):
    answer = Answer.objects.filter(question_id=answer_idx)
    return render(request, "result.html",{'answer':answer})