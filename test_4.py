#!/bin/python3

import sys
import os

# Complete the function below.

def maxDifference(a):
    max=-1
    # for i in range(len(a)):
    #     for j in range(i):
    #         diff=a[i]-a[j]
    #         if diff >0 and diff > max:
    #             max = diff
    # return max
    diff=[]
    length = len(a)
    for i in range(length):
        if i < length-1:
            diff.append(a[i+1]-a[i])
    
    lengthdiff = len(diff)
    for i in range(lengthdiff):
        print(diff[i])

    lengthdiff = len(diff)
    psum = 0
    ret = -1
    for i in range(lengthdiff):
        if psum >= 0 : 
            psum = psum + diff[i]
        else:
            psum = 0 + diff[i]
        if psum > ret:
            ret= psum
        else:
            ret = ret
    max = -7654321 
    for i  in range(lengthdiff):
        if max < diff[i]:
            max = diff[i]
    if max < 0 :
        ret = -1
    return ret
    
if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a_cnt = 0
    a_cnt = int(input())
    a_i = 0
    a = []
    while a_i < a_cnt:
        a_item = int(input())
        a.append(a_item)
        a_i += 1


    res = maxDifference(a);
    f.write(str(res) + "\n")


    f.close()