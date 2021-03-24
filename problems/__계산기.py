import sys
import string
readl = sys.stdin.readline

n = int(readl())

cmd = [list(readl().split()) for _ in range(n)]
alpha_dict = string.ascii_uppercase
for line in cmd:
    base   = int(line[0])
    first  = int(line[1],base)
    second = int(line[2],base)
    if first == 0 or second == 0:
        print(0)
        continue


    temp_ans = first*second


    ans=""
    if temp_ans<0:
        ans+="-"
        temp_ans=-temp_ans
    n=0
    while True:
        if pow(base,n)>temp_ans:
            break
        n+=1
    n-=1

    while True:

        if n==-1:
            break

        qoutient,remainder = divmod(temp_ans,pow(base,n))
        #print(pow(base,n),qoutient,remainder)
        temp_ans-=qoutient*pow(base,n)
        if qoutient>=10:
            qoutient=alpha_dict[qoutient-10]
        ans+=str(qoutient)
        n-=1
    print(ans)





