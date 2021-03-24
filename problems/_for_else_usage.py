

data = [2, 4, 5, 11, 3]

test = 0

for i in data:

    if i>10:

        test=1
        break
if test==0:
    print("10보다 큰 수 없음")



for i in data:
    if i>10:
        break

else:
    print("10보다 큰 수 없음")


