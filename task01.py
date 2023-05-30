#Дан список чисел, определить количество уникальных чисел
# [1,1,2,0,-1,3,4,4]
# 6

import random
list1=[]
n=10
for i in range(n):
    list1.append(random.randint(1,10))
print(list1)
print(len(list(set(list1))))
