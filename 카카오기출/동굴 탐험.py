import sys

n     = 9
path  = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]


def solution(n, path, order):
    rule = dict()
    for a,b in order:
        rule[a]=b

    leaf = [0]*n
    print(leaf)



solution(n,path,order)

