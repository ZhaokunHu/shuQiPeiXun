# coding=utf8
import numpy as np
n=input("Please enter the amount:")
m=input("Please enter the gap:")
i=0
peopleDied=0
counter=0
ring=np.zeros(n)
while(peopleDied!=n-1):
    if(ring[i]==0):
        counter+=1
    if(counter==m):
        counter=0
        ring[i]=1
        print i
        peopleDied+=1
    if(i!=n-1):
        i+=1
    else:
        i=0
for j in range(0,n-1):
    if(ring[j]==0):
        print "the answer is:",j   