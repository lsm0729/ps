import sys

read = sys.stdin.readline

n = int(read())

floor = [list(map(int,read().split())) for _ in range(n)]


floor.sort(key= lambda x : x[1])



#print(floor)


pointer = float('-inf')
ans     = 0
for start, end in floor:
    if pointer < start:
        ans+=1
        pointer = end
        continue
print(ans)
