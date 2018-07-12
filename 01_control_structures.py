import random

points=0
counts=0

for i in range(100):
    while points < 100:
        point_once=int(random.random()*6+1)
        points += point_once
        counts += 1
    points += point_once
    print(point_once,points,counts)
