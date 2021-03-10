"""
https://www.acmicpc.net/problem/12100
"""

import sys
from collections import deque

readl = sys.stdin.readline


n= int(readl())

mm = [list(map(int,readl().split())) for _ in range(n)]

def left():
    for i in range(n):
        line = mm[i]
        new_line = []
        sum=False
        for element in line:
            if element == 0: continue
            if not new_line:
                new_line.append(element)
                continue

            if new_line[-1]== element and sum==False:
                new_line[-1]*=2
                sum = True
            elif new_line[-1]== element and sum==True:
                new_line.append(element)
                sum = False
            else :
                new_line.append(element)
        mm[i]= new_line+[0]*(n-len(new_line))

def right():
    for i in range(n):
        line = mm[i]
        new_line = []
        sum=False
        for element in reversed(line):
            if element == 0: continue
            if not new_line:
                new_line.append(element)
                continue

            if new_line[-1]== element and sum==False:
                new_line[-1]*=2
                sum = True
            elif new_line[-1]== element and sum==True:
                new_line.append(element)
                sum = False
            else :
                new_line.append(element)
        new_line.reverse()
        mm[i]= [0]*(n-len(new_line))+new_line

def up():
    for x in range(n):
        new_line=[]
        sum= False
        for y in range(n):





for line in mm:
    print(line)

right()

for line in mm:
    print(line)














