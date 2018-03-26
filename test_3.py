#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

# Complete the function below.

def  getMovieTitles(substr):
    url="https://jsonmock.hackerrank.com/api/movies/search/?Title="
    url+=substr
    read=json.loads(urlopen(url).read().decode('utf-8'))
    pages=read['total_pages']
    #print(pages)
    arrlist=[]
    for i in range(pages):
        suburl=url+"&page="+str(i+1)
        #print(suburl)
        subread=json.loads(urlopen(suburl).read().decode('utf-8'))
        for j in subread['data']:
            title=j['Title']
            arrlist.append(title)
            #print(title)
    arrlist.sort()
    return arrlist


f = open(os.environ['OUTPUT_PATH'], 'w')
    

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()