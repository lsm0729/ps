from sys import stdin

read = stdin.readline

T = int(read())
n, s = 0, 0
pos = list()


def check(distance: int) -> bool:
    global n, s, pos

    count = 1
    curr = pos[0]

    for v in pos:
        if v >= curr + distance:
            curr = v
            count += 1

            if count == s:
                return True

    return False


def binary_search() -> int:
    global pos
    """
    최소거리값 D를 이분법으로 하여 접근한다.
    min 1 max pos 요소 맨앞뒤값 차이로 설정.
    중간값 mid를 구해 
    
    """
    min = 1
    max = pos[-1] - pos[0]
    while (max - min) >= 2:
        mid = (min + max) // 2

        if not check(mid):
            max = mid
        else:
            min = mid
        print(max,mid,min)

    for v in reversed(range(min,max+1)):
        if check(v): return v
    return min


for _ in range(T):
    n, s = map(int, read().split())
    pos = sorted(list(map(int, read().split())))
    print(binary_search())
