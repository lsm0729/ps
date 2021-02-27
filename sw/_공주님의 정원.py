import sys




def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info



# 입력받는 부분
N, ff = input_data()

# 여기서부터 작성



##TODO: 빠른시작, 느린끝 순으로 정렬

ff = sorted(ff, key = lambda x : (x[0],x[1],x[2], x[3]))
f= []
for a,b,c,d in ff: f.append([100*a+b,100*c+d])

#print(f)

def greedy(f):

    present = 301
    prev    = 0
    count   = 0

    for start, end in f:
        if present<start: return 0

        if present<end  :

            if prev < start:
                prev=present
                present = end
                count+=1

            else: ## start < prev
                present = end

        if 1130<present:
            return count

    return 0


print(greedy(f))