from bwsi_grader.python.three_five import grader


def student_func(input_num):
    if(input_num % 3 == 0 and input_num % 5 == 0):
        return "threefive"
    elif(input_num % 3 == 0):
        return "three"
    elif(input_num % 5 == 0):
        return "five"
    else:
        return input_num


grader(student_func)
