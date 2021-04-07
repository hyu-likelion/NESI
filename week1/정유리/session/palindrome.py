from bwsi_grader.python.palindrome import grader
def student_func(x):
    print(len(x))
    ws = ' '
    x = str(x).lower()
    if ws in x:
        i = 0
        while i < len(x):
            print(i,x)
            if x[i] == ws:
                    x = x[:i] + x[i+1:]
            else:
                i += 1
    if x == x[::-1]:
         result = True
    else:
        result = False
    return result
grader(student_func)
