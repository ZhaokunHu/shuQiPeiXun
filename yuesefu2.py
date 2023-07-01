import numpy as np
n=input("Please enter the amount:")
m=input("Please enter the gap:")
peopleDied=0
ring=np.zeros(n)
def yuesefu(n,m,i):
    if(i==1):
        return (m-1)%n
    else:
        return (m+yuesefu(n-1,m,i-1))%n
for i in range(1,n):
    print yuesefu(n,m,i)
print "answer:",yuesefu(n,m,n)