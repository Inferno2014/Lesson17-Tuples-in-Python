t1 = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,7):
    if t1[i] == 1:
        rainy+=1
    elif t1[i] == 0:
        sunny+=1
if sunny > rainy:
    print('It will be sunny today!')
elif sunny < rainy:
    print('It will be rainy today!')
