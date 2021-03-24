import sys

read = sys.stdin.readline


N= int(read())

ll = [list(map(int,read()[:-1]))   for _ in range(N)]

for num in ll:

    num.sort(reverse=True)
    n1=''
    n2=''
    is_n1 = True
    for n in num:
        if n==6: n=9
        if not n1:
            if n==0 :
                print(0)
                break
            n1+=str(n)
            continue

        if not n2:
            if n==0 :
                print(0)
                break
            n2+=str(n)
            continue

        if n1>n2:
            n2+=str(n)
        else:
            n1+=str(n)
    else:print(int(n1)*int(n2))

