def countingValleys(steps, path):
    level=0
    is_valley = False
    count =  0

    for step in path:

        level=level-1 if step =="D" else (level+1)

        if level>=0 and is_valley==True:
            count+=1
            is_valley=False

        elif level<0 and is_valley==False:
            is_valley=True

    return count



