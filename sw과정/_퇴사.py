"""
https://www.acmicpc.net/problem/14501

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

"""

import sys
readl = sys.stdin.readline

N = int(readl())
## 1일 부터 맞추기위해 앞에 [0,0] 추가
schedule =[[0,0]]+[list(map(int,readl().split())) for _ in range(N)]

#print(schedule)



## 1일에서 N 일까지 + 0일 및 N+1 일 추가 (계산용의상)
max_pay = [0]*(N+2)

## schedule list 기준으로 마지막 N일부터 시작해서 1일까지 역순으로 진행
for  day in range(N,0,-1):
    time = schedule[day][0]
    pay = schedule[day][1]
    #print(time, pay)

    # 기간이 넘어가는 경우
    if day+time>N+1:
        max_pay[day]=max_pay[day+1]
        continue
    ## else
    """
    만약 해당 day가 근무 가능하다면
    max_pay[day]의 계산은
    해당일의 근무를 하지 않는것 max_pay[day+1] (전날까지의 max_pay 값)과
    해당일의 근무를 하는것     max_pay(day+time] + pay
    을 비교해 max값으로 처리
    왜냐하면 day ~ day+time 사이의 pay값에 따라 
    day 에 일을 함에 따라 얻는 이익이 그 day의 time 동안의 pay보다 많을수도
    적을수도 있기 때문. 
    """
    max_pay[day]= max(max_pay[day+time]+pay,max_pay[day+1])

print(max_pay[1])