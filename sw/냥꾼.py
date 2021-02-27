import sys

def input_data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals



# 입력받는 부분
M, N, L, shoots, animals = input_data()

# M 사대 개수
# N 동물 수
# L 사정거리
# shoots 사대위치
# animals 동물 좌표
shoots=sorted(shoots)




def check_single(shoot1,x,y):
    gap = abs(x-shoot1)
    if gap<=L and y<=-gap+L:
        return 1
    else :
        return 0

def check_btw(shoot1,shoot2,x,y):
    gap = min(x-shoot1,shoot2-x)
    if gap<=L and -gap+L>=y:
        return 1
    else:
        return 0





def bs(start,end,target):

    while start<=end :

        mid =(start+end)//2

        if target<shoots[mid]:
            end=mid-1
        elif target>shoots[mid]:
            start =mid+1
        else :
            start = mid
            end   = mid
            break

    return start,end

ans = 0
for x,y in animals:



    right,left = bs(0,M-1,x)


    if left ==-1:
        ans+=check_single(shoots[0],x,y)
        continue
    if  right == M :
        ans+=check_single(shoots[M-1],x,y)
        continue
    if left==right :
        ans+=check_single(shoots[left],x,y)
        continue

    ans += check_btw(shoots[left],shoots[right],x,y)

print(ans)


