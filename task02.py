# Необходимо сделать цикличнае сдвиги элементов списка на k элементов
# [1,2,3,4,5]
# [4,5,1,2,3]

import random
list1=[]
n=10
for i in range(n):
    list1.append(random.randint(1,10))
print(list1)
k= int(input('Введите число сдвигов: '))
count=1
while count<=k:
    list1.insert(0,list1.pop())
    count+=1
print(list1)