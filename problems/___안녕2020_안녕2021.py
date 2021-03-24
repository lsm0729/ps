from sys import stdin
read = stdin.readline

global_candidate_list=[202021,20202021,
           202002021,
           202012021,
           202022021,
           202032021,
           202042021,
           202052021,
           202062021,
           202072021,
           202082021,
           202092021
           ]


T= int(read())
for _ in range(T):
    N= int(read())
    ll = list(map(int,read().split()))
    ans = 0
    numbers = dict()
    for num in ll:
        try:    numbers[num]+=1
        except: numbers[num]=1
    #print("=========================")
    #print(numbers)
    for key,value in numbers.items():
        candidate_list = [x-key for x in global_candidate_list]
        #print(key)
        #print(candidate_list)
        for candi in candidate_list:
            if candi in numbers:
                ans+=numbers[candi]*value
    print(ans//2)














