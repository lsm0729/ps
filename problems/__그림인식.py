import sys
from collections import deque

readl = sys.stdin.readline

n = int(readl())
mm = [list(map(int, readl()[:-1])) for _ in range(n)]
candi = set()
area = dict()
check = [[0]*n for _ in range(n)]
overlapped = set()



for y in range(n):
    for x in range(n):
        color = mm[y][x]

        if color == 0 : continue

        if color in area :
            area[color].append((y,x))
        else             :
            candi.add(color)
            area[color]=[(y,x)]
#for line in mm: print(line)

#print("========================")


for color,pos in area.items():
    #print(color)
    #print(pos)

    y_pos = sorted(pos, key= lambda x: x[0])
    x_pos = sorted(pos, key= lambda x: x[1])


    #print(x_pos)
    #print(y_pos)
    s_y,s_x = y_pos[0][0],x_pos[0][1]
    e_y,e_x = y_pos[-1][0],x_pos[-1][1]

    #print(s_y,s_x)
    #print(e_y,e_x)
    #print("------------------")

    for y in range(s_y,e_y+1):
        for x in range(s_x,e_x+1):
            if color!=mm[y][x]:
                #print(y,x)
                #print(mm[y][x])
                overlapped.add(mm[y][x])

#print(candi)
#print(overlapped)

print(
    len(candi-overlapped)
)




