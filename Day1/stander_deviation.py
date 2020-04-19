# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:11:51 2020

@author: ninjaac
"""

import math
from statistics import mean
N=int(input("enter the no of elements"))
X=list(map(int,input("enter the values").split()))
u=mean(X)
distance_from_mean=0
variance=0
for i in range(0,len(X)):
    distance_from_mean+=(X[i]-u)**2
    average_distance_from_mean=distance_from_mean/N
    variance=average_distance_from_mean
    
SD=round(math.sqrt(variance),1)
print(SD)
#using the statistics modele it become very easy
#there are two function in standared deviation
###stdev() fine SD on sample of population
###pstdev() find the SD on whole population
from statistics import pstdev,variance
SD=pstdev(X)
variance=variance(X)
