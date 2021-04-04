def p32():
    str=input().upper()
    a={}
    for i in str:
        if i in a:
            a[i]+=1
        else:
            a[i]=1

    max_value=0
    result =-1
    for i in a:
        if a[i]>max_value:
            max_value=a[i]
            result=i
        elif a[i]==max_value:
            result='?'
    print(result)
p32()

