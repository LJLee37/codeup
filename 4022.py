import math
D = int(input())
H = int(input())
if D >= 120:
    transport = math.ceil(D / 10) * 1000
    if H is 1:
        print(25000 + transport)
        exit()
    sleep = 40000 * (H - 1)
    food = (3 * (H - 1) + 1) * 5000
    dayPay = 0
    i = 0
    while H > 0:
        min = 0
        if i == 0 or i == 1:
            min = 15
        elif i == 2:
            min = 30
        else:
            dayPay += 7000 * H
            break
        if H >= min:
            dayPay += 1000 * min * (10 - i)
            H -= min
        else:
            dayPay += 1000 * H * (10 - i)
            break
        i += 1
    print(sleep + food + dayPay + transport)
else:
    print(H * 1000 * (25 + math.ceil(D / 10)))
