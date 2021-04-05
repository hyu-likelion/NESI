A,B=input().split()
A= int(A)
B= int(B)

def bigyo (x,y):
    if (x>y):
        print ('>')
    elif (x<y):
        print ('<')
    else:
        print ('==')

bigyo(A,B)