# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f=open("C:/Users/bpandey/.spyder-py3/src/concat.csv","r").read().split("\n")
g=[]
for each in f:
    g.append(each.split(","))
for each in g:
    print(each)