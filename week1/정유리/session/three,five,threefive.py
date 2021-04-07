def student_func(x):
    if x%3 == 0:
        result = 'three'
        if x%5 == 0:
            result += 'five'
    elif x%5 == 0:
        result ='five'
    else:
        result = x
    return result