# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N, S, M = map(int, readl().split())
    return N, S, M


sol_list = []

# 입력받는 부분
N, S, M = input_data()

person = list(x + 1 for x in range(N))
person = deque(person)
S = S - 1


##print(type(person))

while person:
    presentone = person[(S + M-1) % N]
    nextone = person[(S + M) % N]

    ##print(presentone,nextone)
    sol_list.append(presentone)
    person.remove(presentone)
    if not person:
        break
    S = person.index(nextone)
    N -=1

print(*sol_list)
