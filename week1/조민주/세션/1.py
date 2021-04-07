from bwsi_grader.python.three_five import grader
def student_func(number):
    if (number%5==0):
        if (number%3==0):
            c="threefive"
            print (c)
            return c
        else:
            c="five"
            print (c)
            return c
    elif (number%3==0):
        c="three"
        print (c)
        return c
    else:
        print (number)
        return number
        pass 
grader(student_func)
