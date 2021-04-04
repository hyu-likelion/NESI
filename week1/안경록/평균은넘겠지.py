def p22():
    testcase=int(input())


    for i in range (0,testcase):
        score = list(map(int, input().split()))
        total=int(0)
        count=int(0)
        for j in range(1,score[0]+1):
            total+=score[j]
        total//=score[0]

        for j in range(1,score[0]+1):
            if total < score[j]:
                count+=1
        result=float((count/score[0])*100)
        result = round(result,3)

        print(f'{result:.3f}%')


p22()
