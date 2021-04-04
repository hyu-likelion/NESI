def p4():
    a,b = input().split()
    a = int(a[::-1])    #뒤집어주는 방법.
    b = int(b[::-1])

    if a>b:
        print(a)
    else:
        print(b)


p4()