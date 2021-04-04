def p3():
    number = input()
    numlist = list(map(int,input().split()))

    print("{} {}".format(min(numlist),max(numlist)))


p3()