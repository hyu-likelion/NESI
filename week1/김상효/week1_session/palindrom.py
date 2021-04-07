from bwsi_grader.python.palindrome import grader


def student_func(input_val):
    munjang = ""
    word_list = input_val.lower().split()
    for i in word_list:
        munjang += i

    half = int(len(munjang)/2)
    for i in range(half):
        if(munjang[i] == munjang[len(munjang) - 1 - i]):
            pass
        else:
            return False

    return True


grader(student_func)
