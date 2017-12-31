# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

line=open("C:/Users/bpandey/.spyder-py3/src/concat.csv","r").read().split("\n")
item=[]
dict={}
for each in line:
    item.append(each.split(","))
for each in item[1:len(item)-1]:
    if (each[1] not in dict) :
        dict[each[1]]=1
    else:
        dict[each[1]] = dict[each[1]]+1
print(dict)
    
    
