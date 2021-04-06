def overAverage():
    C = int(input())
    for n in range(C):
        score = input().split()
        student = int(score[0])
        sum = 0
        count = 0
        for i in range(1, student + 1):
            sum += int(score[i])
        average = sum / student
        for i in range(1, student + 1):
            if int(score[i]) > average:
                count += 1
                print(count)
        print('%.3f' % (count / student * 100) , '%' , sep = '')
        
overAverage()
