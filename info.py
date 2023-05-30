first_list = [9, 'fkr' , True, [1,2,3]]

# for element in first_list:
#     print(element)

# for i, element in enumerate(first_list):
#     if element ==9:
#         first_list[i]='nine'

# print(first_list.index(1))

# print(first_list)
# first_list.remove('fkr')
# print(first_list)

second_list= [1,5,23,98,12,5,7,3]
# print(second_list)
# second_list.sort(reverse=True)
# print(second_list)
# second_list.sort(reverse=False)
# print(second_list)

# print(sorted(second_list))
# print(second_list)

# a=[1,1,1,1,2,2,2,1,34,34,34,1,2,2,2,6,3,7,55,6,5,5,3,1]     #очистка списка от дубликатов
# print(list(set(a)))

#СЛОВАРИ

first_dict={'Mother' : 2345, 'Father':23451, 'friend': 234256}
for key in first_dict:
    print(first_dict[key])

print(first_dict.get('Mother'))