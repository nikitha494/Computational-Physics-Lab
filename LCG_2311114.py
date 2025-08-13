#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 16:01:44 2025

@author: nikitha
"""
import matplotlib.pyplot as plt
a = 1103515245
c = 12345
m = 32768
X=[]
Y=[]
def LCG(a,c,m):
    x=0.1
    for i in range(0,1000):
        x=(a*x+c)%m
        X.append(x)
    x=X[4]
    for i in range (0,1000):
        x=(a*x+c)%m
        Y.append(x)
    return(X,Y)
LCG(a,c,m)
def Plot(x, y , title='LCGplot', xlabel='x_i', ylabel='x_i+5',file_name='LCG_plot.png'):
    plt.plot(x, y, marker='o', linestyle='', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)  
    plt.savefig(file_name)
    plt.show()
Plot(X, Y)