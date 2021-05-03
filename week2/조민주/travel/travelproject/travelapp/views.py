from django.shortcuts import render
from travelapp.models import Survey,Result

# Create your views here.
def home(request):
    survey = Survey.objects.order_by('-survey_idx')[0]
    return render(request, "travelapp/home.html",{'survey':survey})

def save_result(request):
    survey_idx = request.POST["survey_idx"]
    dto = Result(survey_idx=int(request.POST["survey_idx"]), ans=request.POST["num"])
    dto.save()
    return render(request, "travelapp/success.html")

def show_result(request,question_id):
    answer = Result.objects.filter(survey_idx=question_id)
    return render(request, "travelapp/result.html", {'answer': answer})