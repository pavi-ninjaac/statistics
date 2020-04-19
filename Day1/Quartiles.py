# -*- coding: utf-8 -*-

"""
Created on Sat Apr 18 22:16:37 2020

@author: ninjaac
"""
from statistics import median
X=[]
N=int(input("enter the no of elements"))
X=list(map(int,input("enter the values").split()))
X.sort()
len=len(X)
Q1=0
Q2=0
Q3=0
if not (len%2==0):
    Q2=int(median(X))
    Q2_index=X.index(Q2)
    L=X[0:Q2_index]
    U=X[Q2_index+1:]
    Q1=int(median(L))
    Q3=int(median(U))
else:
    Q2=int(median(X))
    center=len//2
    L=X[0:center]
    U=X[center:]
    Q1=int(median(L))
    Q3=int(median(U))
    
print(Q1)
print(Q2)
print(Q3)
    
