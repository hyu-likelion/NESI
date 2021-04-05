def scoring():
    C=int(input())
    tables = [list(map(int,input().split())) for c in range(C)]
    
    for i in range(C):
        number=tables[i][0]
        hap=0
        for d in range(1,number+1):
            hap=hap+tables[i][d]
        average=hap/number
        print ("{:.3f}%".format(average))

scoring()

