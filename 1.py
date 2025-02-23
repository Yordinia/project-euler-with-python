# 1
sum = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        factor = 3 if i%3==0 else 5
        print(' found factor .. of ', factor, ' which is - ', i)
        sum += i
print('final val = ' , sum)