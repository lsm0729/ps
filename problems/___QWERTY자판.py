
import sys
read = sys.stdin.readline

alpha_dict= dict()
key= ['QWERTYUIOP',
      'ASDFGHJKL',
      'ZXCVBNM']
for row_idx,line in enumerate(key):
    for col_idx, s in enumerate(line):
        alpha_dict[s]=(row_idx, col_idx)

n = int(read())
order_list = [list((read()[:-1])) for _ in range(n)]
for case in order_list:
    print("==================")
    print(case)
    ans=0
    prev = case[0]
    y_,x_ = alpha_dict[prev]
    print(prev,y_,x_)
    for s in case:
        print("----------")
        print(s)
        if prev==s:
            ans+=1
            print(y_,x_,1)
            continue
        y,x = alpha_dict[s]

        ans=ans+2*(abs(y-y_)+abs(x-x_))+1
        print(y,x,2*(abs(y-y_)+abs(x-x_))+1)
        y_,x_ = y,x
        prev=s
    print(ans)













