from bwsi_grader.python.palindrome import grader
def student_func(naming):
    naming=naming.replace(" ","")
    c=len(naming)
    naming=naming.lower()
    naming=list(naming)
    #짝수일 때
    a=0
    b=c/2
    d=(c-1)/2
    b=int(b)
    d=int(d)
    if (c%2==0):
        for i in range(b):
            if (naming[i]==naming[c-i-1]):
                a=a+1
            else:
                break
        if (a==b):
            return True
        else:
            return False
    #홀수일 때
    else:
        for i in range(d):
            if (naming[i]==naming[c-i-1]):
                a=a+1
            else:
                break
        if (a==d):
            return True
        else:
            return False
    
#student_func()
grader(student_func)