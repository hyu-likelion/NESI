from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Survey, Result

# Create your views here.
def home(request):
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request, "home.html",{'survey':survey})

@csrf_protect
def save_result(request):
    survey_idx = request.POST["survey_idx"]
    dto = Result(survey_idx=int(request.POST["survey_idx"]), ans=request.POST["num"])
    dto.save()
    return render(request, "success.html")

@csrf_protect
def show_result(request,question_id):
    answer = Result.objects.filter(survey_idx=question_id)
    return render(request, "result.html", {'answer': answer})