'''
a = 1
b = 2
i = 0
while(i <= 2):
    print(i)
    i += 1

'''

''' list
list = ['dog','cat','cow']
print("here is a list")
print(list)

print("list[0:2]: ", str(list[0:2])) #

del list[0:2]
print("after delete: " + str(list))  #string

list1 = [1,2,3,4,5]
print("list1: ")
print(list1)

print(list + list1)

for x in list1: print(x, end="QAQ")	
'''

'''tuple
tuple = ("tuple",2,23)
print(tuple)
for x in tuple: print(x, end=" ")
print()
'''

''' dictionary
test_dict = {'name':'dudu', 'age':21, 'favorite_fruit':'Banana'}
print(test_dict)
print("dict length:",len(test_dict))
print('name:',test_dict['name'])
'''

''' input
a = input("Please enter your words\n")
print(a)
#input more elements
b,c,d = (input("Please enter three elements").split())
print(b,c,d)
'''

set1 = {1,2,4,6,8}
set2 = {5,23,76,32,4}
set1.add(23)
print("set1i set2", set1 | set2)
print("set1 & set2", set1 & set2)
print("set1 - set2", set1 - set2)



