# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:34:05 2020

@author: ninjaac
"""
N=int(input("enter the no of elements"))
X=list(map(int,input("enter the values").split()))
W=list(map(int,input("enter the wieghts").split()))
upper=0
lower=0
for i,j in zip(X,W):
    upper+=i*j
    lower+=j
    weighted_mean=upper/lower
    weighted_mean=round(weighted_mean,1)
print(weighted_mean)
