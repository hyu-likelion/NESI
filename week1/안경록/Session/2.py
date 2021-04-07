from bwsi_grader.python.palindrome import grader

def func(x):
    x = x.lower()
    x = str(x)
    x = x.replace(" ", "")

    y=list(x)
    x=list(x)
    y.reverse()
    if x==y:
        return True
    else:
        return False
    pass


grader(func)
