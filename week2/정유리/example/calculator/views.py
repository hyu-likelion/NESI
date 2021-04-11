from django.shortcuts import render

def main(request):
    return render(request, "main.html")
    # 메인페이지 렌더링

def calculator(request):
    a = request.GET['text']
    result = eval(a)
    return render(request, "calculator.html", {'result':result})
    # GET으로 값을 받고, eval 함수를 사용해 값 계산
    # calculator 페이지 렌더링
