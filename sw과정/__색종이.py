import sys

read = sys.stdin.readline

n = int(read())

mm = [list(map(int,read()[:-1])) for _  in range(n)]
check = [[0]*n for _ in range(n)]
area= dict()



for y in range(n):
    for x in range(n):
        color = mm[y][x]
        if color == 0 : continue
        try   : area[color].append((y,x))
        except: area[color]=[(y,x)]

for color,pos in area.items():
    y_pos = sorted(pos, key= lambda x: x[0])
    x_pos = sorted(pos, key= lambda x: x[1])
    s_y,s_x = y_pos[0][0],x_pos[0][1]
    e_y,e_x = y_pos[-1][0],x_pos[-1][1]

    for y in range(s_y,e_y+1):
        for x in range(s_x,e_x+1):
            check[y][x]+=1

ans = 0
for line in check:
    temp = max(line)
    ans  = max(ans,temp)
print(ans)



