from bwsi_grader.python.three_five import grader


def student_func(x):

    answer=""
    if x%3==0 and x%5==0:
        answer+="threefive"
        return answer
    elif x%3==0:
        answer += "three"
        return answer
    elif x%5==0:
        answer += "five"
        return answer
    else:
        return x
    pass



grader(student_func)