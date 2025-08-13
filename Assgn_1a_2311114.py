#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 15:28:16 2025

@author: nikitha
"""
import matplotlib.pyplot as plt

x=0.1
c=2.986
k=7
X=[]
Y=[]
def random_number(c,x,k):
    x=0.1
    for i in range (0,1000):
        x=c*x*(1-x)
        X.append(x)
    x=X[k+1]
    for i in range(0,1000):
        x=c*x*(1-x)
        Y.append(x)
    return X,Y
random_number(c,x,k)
def Plot(x, y , title, xlabel='x_i', ylabel='x_i+k',file_name='random_plot3.png'):
    plt.plot(x, y, marker='o', linestyle='', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)  
    plt.savefig(file_name)
    plt.show()
N='Plot for c=',c,'k=',k
Plot(X, Y, N)
#print(len(X),len(Y))