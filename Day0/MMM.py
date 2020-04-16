# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:13:20 2020

@author: pavi-ninjaac
"""
import numpy as np
X=[]
N=int(input("enter the no of elements"))
X=list(map(int,input("enter the values").split()))
X.sort()
#mean 
add=0    
for i in range(0,N):
   add+=X[i]
mean=add/N
# find the median

len=len(X)
if not len%2==0:
    median=(len//2)
    median=X[median]
else:
    a=len//2
    median1=X[a]
    median2=X[a-1]
    median=(median1+median2)/2
    
#find the mode
most_frequent=0
num=0
for i in X:
    fre=X.count(i)
    if(most_frequent<fre):
        most_frequent=fre
        num=i
print(mean)
print(median)
print(num)        
#using stastics module
from statistics import mean,median,mode

#find the mean
mean=mean(X)

#find the median
median=median(X)

#find the mode
mode=mode(X)
