import random

a1=0
count=0
for i in range(100):
   a=random.random()
   a1 += a  # is same like a1=a1+a
   count += 1
   #print(a,a1,count)
print('the sum of 100 random numbers is ', a1)
