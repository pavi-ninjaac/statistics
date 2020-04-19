# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:40:39 2020

@author: ninjaac
"""

from statistics import median
from math import ceil
X=[]
N=int(input("enter the no of elements"))
X=list(map(int,input("enter the values").split()))
F=list(map(int,input("enter the frequency").split()))
#making the dataset S
S=[]
a=[]
for i,j in zip(X,F):
    a=[i]*j
    for z in a:
        S.append(z)

S.sort()
len=len(S)
Q1=0
Q2=0
Q3=0
if not (len%2==0):
    Q2=ceil(median(S))
    Q2_index=(len//2)
    L=S[0:Q2_index]
    U=S[Q2_index+1:]
    Q1=ceil(median(L))
    Q3=ceil(median(U))
else:
    Q2=ceil(median(S))
    center=len//2
    L=S[0:center]
    U=S[center:]
    Q1=ceil(median(L))
    Q3=ceil(median(U))
    
Q1=round(Q1,1)
Q2=round(Q2,1)
Q3=round(Q3,1)

dif=Q3-Q1
interQuartileRange=float(dif)
interQuartileRange=round(interQuartileRange,1)
print(interQuartileRange)   


