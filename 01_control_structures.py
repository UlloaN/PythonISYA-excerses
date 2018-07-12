import random
import math as mt
#a=[]
c=0
for i in list(range(100)):
    points=0
    counts=0
    while points < 100:
        point_once=int(random.random()*6+1)
        points += point_once
        counts += 1
    i += 1 #for count the iterations
#    a.append(counts) to save in a list
    c += counts
average=c/i
average=int(average)
#print(point_once,points,counts,c,i,average) # to test
print('The average of have a minimun 100 points when you thrown a die is:', average, 'times') 
