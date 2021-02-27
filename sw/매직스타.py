import sys
from string import ascii_uppercase
def input_data():
    readl = sys.stdin.readline
    map_star = [list(readl().strip()) for _ in range(5)]
    return map_star


# 입력받는 부분
mm = input_data()

alpha_dict = {}
alpha_list= ' '+ascii_uppercase
c = 1
for A in ascii_uppercase:
    alpha_dict[A]=c
    c+=1
alpha_dict['x']=0
alpha_dict['.']=0


'''
l1= [mm[0][4],mm[1][3],mm[2][2],mm[3][1]]
l2= [mm[0][4],mm[1][5],mm[2][6],mm[3][7]]

l3= [mm[1][1],mm[1][3],mm[1][5],mm[1][7]]

l4= [mm[1][1],mm[2][2],mm[3][3],mm[4][4]]
l5= [mm[1][7],mm[2][6],mm[3][5],mm[4][4]]

l6= [mm[3][1],mm[3][3],mm[3][5],mm[3][7]]
'''

#ll=[l1,l2,l3,l4,l5,l6]


## 체크해야할 라인
ll=[
    [(0,4),(1,3),(2,2),(3,1)],
    [(0,4),(1,5),(2,6),(3,7)],
    [(1,1),(1,3),(1,5),(1,7)],
    [(1,1),(2,2),(3,3),(4,4)],
    [(1,7),(2,6),(3,5),(4,4)],
    [(3,1),(3,3),(3,5),(3,7)]
    ]

## 현재 라인별 sum
sum_chk =[]
## 라인별 겹치는 라인
sum_chk_dict={0:(0,1,2,3,5),
              1:(0,1,2,4,5),
              2:(0,1,2,3,4),
              3:(0,2,3,4,5),
              4:(1,2,3,4,5),
              5:(0,2,3,4,5)}
## 사전순 배열 체크
order_chk_candi = [(0,4),
         (1,1),(1,3),(1,5),(1,7),
         (2,2),(2,6),
         (3,1),(3,3),(3,5),(3,7),
         (4,4)]

order_chk=[]
used_alphabet_chk=[0]*13
for y,x in order_chk_candi:
    used_alphabet_chk[alpha_dict[mm[y][x]]] = 1
    if mm[y][x]=='x':
        order_chk.append((y,x))
del order_chk_candi








def chk_sum(l):
    sum=0
    for y,x in l:
        sum+=alpha_dict[mm[y][x]]
    return sum

for l in ll:
    sum_chk.append(chk_sum(l))

def chk_sum_per_point(y,x):

    for line in ll:
        #해당 좌표가 있는 라인
        if (y,x) in line :
            #해당 라인 sum이 26초과면 False
            if chk_sum(line)>26:return False
            #다채워졌는데 26아니면 False
            if 'x' not in line:
                if chk_sum(line)!=26 : return False

    return True





'''
alpha_dict : 알파벳 > 숫자
alpha_list : 숫자   > 알파벳
'''





def dfs(order_chk_idx,cnt):
    global mm
    global used_alphabet_chk
    print('----------------')
    print(cnt)
    if cnt==12:

        for line in mm:
            print(line)

        return



    ## 체크해야될 y,x
    y, x = order_chk[order_chk_idx]

    #A부터 L 까지 체크
    for used_alphabet_chk_idx in range(1,13):

        ## 사용된 알파벳이면 continue
        if used_alphabet_chk[used_alphabet_chk_idx]==1 : continue

        ##체크한후 (포인트가 들어간 라인 합이 26이하인가?
        mm[y][x]=alpha_list[used_alphabet_chk_idx]
        if not chk_sum_per_point(y,x):
            mm[y][x] = 'x'
            continue

        used_alphabet_chk[used_alphabet_chk_idx]=1
        dfs(order_chk_idx+1,cnt+1)
        mm[y][x] = 'x'
        used_alphabet_chk[used_alphabet_chk_idx]=0

print(order_chk)
print(used_alphabet_chk)




dfs(0,0)










