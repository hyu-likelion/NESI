from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
# Create your views here.


def home(request):

    questions = Question.objects.all()
    return render(request, "survey/home.html", {'questions': questions})


def detail(request, id):
    if request.method == 'GET':
        question = get_object_or_404(Question, survey_idx=id)
        return render(request, "survey/detail.html", {'question': question})

    elif request.method == 'POST':
        ans = Answer(survey_idx=id, answer=request.POST['num'])
        ans.save()
        return render(request, "survey/success.html")


def results(request, id):
    answers = Answer.objects.filter(survey_idx=id)
    return render(request, "survey/results.html", {'answers': answers})
