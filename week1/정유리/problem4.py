def reverse():
    A,B = input().split()
    if A[::-1] > B[::-1]:
        print(A[::-1])
    else:
        print(B[::-1])

reverse()
