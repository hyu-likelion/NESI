from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "home.html")

def calculator(request):
    calculates = request.GET['calculate']
    end=eval(calculates)
    return render(request,"result.html",{'ans':end})
    # GET으로 값을 받고, eval 함수를 사용해 값 계산
    # calculator 페이지 렌더링