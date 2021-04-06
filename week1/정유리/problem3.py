def minMax():
    N = int(input())
    num = input().split()
    min = 1000000
    max = -1000000
    for i in range(N):
        if max < int(num[i]):
            max = int(num[i])
        if min > int(num[i]):
            min = int(num[i])
    print(min,max)

minMax()
